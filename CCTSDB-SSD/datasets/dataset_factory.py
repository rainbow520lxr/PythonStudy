# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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
"""A factory-pattern class which returns classification image/label pairs."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datasets import cifar10
from datasets import imagenet

from datasets import pascalvoc_2007
from datasets import pascalvoc_2012

datasets_map = {
    'cifar10': cifar10,
    'imagenet': imagenet,
    'pascalvoc_2007': pascalvoc_2007,
    'pascalvoc_2012': pascalvoc_2012,
}


def get_dataset(name, split_name, dataset_dir, file_pattern=None, reader=None):
    """Given a dataset name and a split_name returns a Dataset.

    Args:
        name: String, the name of the dataset.           数据集的名字
        split_name: A train/test split name.             划分测试集和训练集
        dataset_dir: The directory where the dataset files are stored.    数据集文件存储的位置
        file_pattern: The file pattern to use for matching the dataset source files.    匹配数据集资源文件使用的文件模式
        reader: The subclass of tf.ReaderBase. If left as `None`, then the default
            reader defined by each dataset is used.          tf.ReaderBase的子类，如果为空，则默认为的reader由每个被使用的数据集所定义
    Returns:
        A `Dataset` class.     返回一个数据集的类
    Raises:
        ValueError: If the dataset `name` is unknown.      如果这个数据集的名字未知，报值错误
    """
    if name not in datasets_map:                     #这个不会发生哈
        raise ValueError('Name of dataset unknown %s' % name)
    return datasets_map[name].get_split(split_name,
                                        dataset_dir,
                                        file_pattern,
                                        reader)
