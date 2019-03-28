# Copyright 2015 Paul Balanca. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Implement some custom layers, not provided by TensorFlow.

Trying to follow as much as possible the style/standards used in
tf.contrib.layers
"""
import tensorflow as tf

from tensorflow.contrib.framework.python.ops import add_arg_scope
from tensorflow.contrib.layers.python.layers import initializers
from tensorflow.contrib.framework.python.ops import variables
from tensorflow.contrib.layers.python.layers import utils
from tensorflow.python.ops import nn
from tensorflow.python.ops import init_ops
from tensorflow.python.ops import variable_scope


def abs_smooth(x):
    """Smoothed absolute function. Useful to compute an L1 smooth error.

    Define as:
        x^2 / 2         if abs(x) < 1
        abs(x) - 0.5    if abs(x) > 1
    We use here a differentiable definition using min(x) and abs(x). Clearly
    not optimal, but good enough for our purpose!
    """
    absx = tf.abs(x)
    minx = tf.minimum(absx, 1)
    r = 0.5 * ((absx - 1) * minx + absx)
    return r


@add_arg_scope
def l2_normalization(
        inputs,
        scaling=False,
        scale_initializer=init_ops.ones_initializer(),
        reuse=None,
        variables_collections=None,
        outputs_collections=None,
        data_format='NHWC',
        trainable=True,
        scope=None):
    """Implement L2 normalization on every feature (i.e. spatial normalization).
        实现在每个特征图上的L2正则化
    Should be extended in some near future to other dimensions, providing a more
    flexible normalization framework.
    应该在不久的将来会被扩展到其他维度，会提供更多的正则化框架
    Args:
      inputs: a 4-D tensor with dimensions [batch_size, height, width, channels].
      scaling: whether or not to add a post scaling operation along the dimensions
        which have been normalized.
      输入：一个4D的张量带有的维度[batch_size, height, width, channels]
      规模:是否要添加一个后缩放操作在需要正则化的维度之间
      scale_initializer: An initializer for the weights.
      reuse: whether or not the layer and its variables should be reused. To be
        able to reuse the layer scope must be given.
      规模初始化：一个对于权重的初始化器
      variables_collections: optional list of collections for all the variables or
        a dictionary containing a different list of collection per variable.
      变量集合：对于所有变量或者一个字典（包含每个变量的集合的不同列表）可选择的集合列表
      outputs_collections: collection to add the outputs.
      输出集合：添加输出的集合
      data_format:  NHWC or NCHW data format.
      数据格式：NHWC 或者 NCHW 数据格式
      trainable: If `True` also add variables to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
      scope: Optional scope for `variable_scope`.
      可训练的：如果是true也可以添加变量到图集合中（GraphKeys.TRAINABLE_VARIABLES）
      作用域：对于"变量的作用域"的可选择的作用域
    Returns:
      A `Tensor` representing the output of the operation.
      一个"张量"代表操作的输出
    """

    with variable_scope.variable_scope(
            scope, 'L2Normalization', [inputs], reuse=reuse) as sc:
        inputs_shape = inputs.get_shape()
        inputs_rank = inputs_shape.ndims
        dtype = inputs.dtype.base_dtype
        if data_format == 'NHWC':
            # norm_dim = tf.range(1, inputs_rank-1)
            norm_dim = tf.range(inputs_rank-1, inputs_rank)
            params_shape = inputs_shape[-1:]
        elif data_format == 'NCHW':
            # norm_dim = tf.range(2, inputs_rank)
            norm_dim = tf.range(1, 2)
            params_shape = (inputs_shape[1])

        # Normalize along spatial dimensions.
        outputs = nn.l2_normalize(inputs, norm_dim, epsilon=1e-12)
        # Additional scaling.
        if scaling:
            scale_collections = utils.get_variable_collections(
                variables_collections, 'scale')
            scale = variables.model_variable('gamma',
                                             shape=params_shape,
                                             dtype=dtype,
                                             initializer=scale_initializer,
                                             collections=scale_collections,
                                             trainable=trainable)
            if data_format == 'NHWC':
                outputs = tf.multiply(outputs, scale)
            elif data_format == 'NCHW':
                scale = tf.expand_dims(scale, axis=-1)
                scale = tf.expand_dims(scale, axis=-1)
                outputs = tf.multiply(outputs, scale)
                # outputs = tf.transpose(outputs, perm=(0, 2, 3, 1))

        return utils.collect_named_outputs(outputs_collections,
                                           sc.original_name_scope, outputs)


@add_arg_scope
def pad2d(inputs,
          pad=(0, 0),
          mode='CONSTANT',
          data_format='NHWC',
          trainable=True,
          scope=None):
    """2D Padding layer, adding a symmetric padding to H and W dimensions.   2D填充层， 在H和W的维度上对称填充

    Aims to mimic padding in Caffe and MXNet, helping the port of models to
    TensorFlow. Tries to follow the naming convention of `tf.contrib.layers`.

    Args:
      inputs: 4D input Tensor;
      pad: 2-Tuple with padding values for H and W dimensions;
      mode: Padding mode. C.f. `tf.pad`
      data_format:  NHWC or NCHW data format.
    """
    with tf.name_scope(scope, 'pad2d', [inputs]):
        # Padding shape.
        if data_format == 'NHWC':           #设置为 “NHWC” 时，排列顺序为 [batch, height, width, channels]
            paddings = [[0, 0], [pad[0], pad[0]], [pad[1], pad[1]], [0, 0]]
        elif data_format == 'NCHW':         #设置为 “NCHW” 时，排列顺序为 [batch, channels, height, width]
            paddings = [[0, 0], [0, 0], [pad[0], pad[0]], [pad[1], pad[1]]]
        net = tf.pad(inputs, paddings, mode=mode)
        return net


@add_arg_scope
def channel_to_last(inputs,
                    data_format='NHWC',
                    scope=None):
    """Move the channel axis to the last dimension. Allows to
    provide a single output format whatever the input data format.

    Args:
      inputs: Input Tensor;
      data_format: NHWC or NCHW.
    Return:
      Input in NHWC format.
    """
    with tf.name_scope(scope, 'channel_to_last', [inputs]):
        if data_format == 'NHWC':
            net = inputs
        elif data_format == 'NCHW':
            net = tf.transpose(inputs, perm=(0, 2, 3, 1))
        return net
