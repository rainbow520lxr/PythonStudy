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
"""Converts Pascal VOC data to TFRecords file format with Example protos.
    转换Pascal VOC 格式的数据成TFRecords样本原型的文件格式
The raw Pascal VOC data set is expected to reside in JPEG files located in the
directory 'JPEGImages'. Similarly, bounding box annotations are supposed to be
stored in the 'Annotation directory'
原始的Pascal VOC 数据集是被期望以JPEG文件放在JPEGImages的目录下。同样，bbox注释期望存在Annotation目录下

This TensorFlow script converts the training and evaluation data into
a sharded data set consisting of 1024 and 128 TFRecord files, respectively.
这个tensorflow脚本把训练和评估数据转换成一个共享数据集其中分别包含了1024个128个TFRecord文件

Each validation TFRecord file contains ~500 records. Each training TFREcord
file contains ~1000 records. Each record within the TFRecord file is a
serialized Example proto. The Example proto contains the following fields:
每个有效的TFRecord文件包含了约500个records.每个训练TFRecord文件包含约1000个records.TFrecod文件中的每个record
是一个序列化的样本原型。这个样本原型包含了以下几个字段。

    image/encoded: string containing JPEG encoded image in RGB colorspace
    image/height: integer, image height in pixels
    image/width: integer, image width in pixels
    image/channels: integer, specifying the number of channels, always 3
    image/format: string, specifying the format, always'JPEG'


    image/object/bbox/xmin: list of float specifying the 0+ human annotated
        bounding boxes
    image/object/bbox/xmax: list of float specifying the 0+ human annotated
        bounding boxes
    image/object/bbox/ymin: list of float specifying the 0+ human annotated
        bounding boxes
    image/object/bbox/ymax: list of float specifying the 0+ human annotated
        bounding boxes
    image/object/bbox/label: list of integer specifying the classification index.
    image/object/bbox/label_text: list of string descriptions.

Note that the length of xmin is identical to the length of xmax, ymin and ymax
for each example.
注意的是xmin的长度要和xmax,ymin和ymax对于每个样本都要相同
"""
import os
import sys
import random

import numpy as np
import tensorflow as tf

import xml.etree.ElementTree as ET

from datasets.dataset_utils import int64_feature, float_feature, bytes_feature
from datasets.pascalvoc_common import VOC_LABELS

# Original dataset organisation. 原始数据的结构
DIRECTORY_ANNOTATIONS = 'Annotations/'
DIRECTORY_IMAGES = 'JPEGImages/'

# TFRecords convertion parameters.  TFRecord转换参数
RANDOM_SEED = 4242
SAMPLES_PER_FILES = 200


def _process_image(directory, name):
    """Process a image and annotation file. 处理一个图片和标注文件

    Args:
      filename: string, path to an image file e.g., '/path/to/example.JPG'.  一个图片文件的路径  String格式
      coder: instance of ImageCoder to provide TensorFlow image coding utils.  实例化的编码器， 为了给tensorflow image提供编码工具
    Returns:
      image_buffer: string, JPEG encoding of RGB image.  RGB图像的JPEG的编码   STRING
      height: integer, image height in pixels.             单位为像素的图片高度  integer
      width: integer, image width in pixels.                单位为像素的图片宽度  integer
    """
    # Read the image file.    读取图片文件
    filename = os.path.join(directory, DIRECTORY_IMAGES, name + '.jpg')      #图片文件的全路径名
    print("imgfilename:", filename)
    image_data = tf.gfile.FastGFile(filename, 'rb').read()       #加载图片数据

    # Read the XML annotation file.                     #读取xml标注文件
    filename = os.path.join(directory, DIRECTORY_ANNOTATIONS, name + '.xml')
    print("xmlfilename:", filename)
    tree = ET.parse(filename)                  #获取XML文件的树结构
    root = tree.getroot()                      #获取树的根节点

    # Image shape.
    size = root.find('size')                   #获取根的儿子节点size
    shape = [int(size.find('height').text),
             int(size.find('width').text),
             int(size.find('depth').text)]

    # Find annotations.
    bboxes = []
    labels = []
    labels_text = []
    difficult = []   #这个不需要
    truncated = []   #这个不需要
    for obj in root.findall('object'):      #对根节点搜索为obj的儿子节点
        label = obj.find('name').text
        labels.append(int(VOC_LABELS[label][0]))
        labels_text.append(label.encode('ascii'))    #装入labels的是类别编号，装入labels_text的是类别备注文本编码成ascii码文


        if obj.find('difficult'):                               #没有
            difficult.append(int(obj.find('difficult').text))
        else:
            difficult.append(0)
        if obj.find('truncated'):
            truncated.append(int(obj.find('truncated').text))
        else:
            truncated.append(0)                                 #没有

        bbox = obj.find('bndbox')
        bboxes.append((float(bbox.find('ymin').text) / shape[0],
                       float(bbox.find('xmin').text) / shape[1],
                       float(bbox.find('ymax').text) / shape[0],
                       float(bbox.find('xmax').text) / shape[1]
                       ))
        # bboxes.append((max(float(bbox.find('ymin').text) / shape[0], 0.0),
        #                max(float(bbox.find('xmin').text) / shape[1], 0.0),
        #                min(float(bbox.find('ymax').text) / shape[0], 1.0),
        #                min(float(bbox.find('xmax').text) / shape[1], 1.0)
        #                ))
    return image_data, shape, bboxes, labels, labels_text, difficult, truncated


def _convert_to_example(image_data, labels, labels_text, bboxes, shape,
                        difficult, truncated):
    """Build an Example proto for an image example.  对于一张图片样例创建一个样例原型

    Args:
      image_data: string, JPEG encoding of RGB image;     JPEG编码格式的RGB图片
      labels: list of integers, identifier for the ground truth;    类别码标签集合
      labels_text: list of strings, human-readable labels;          类别标签集合
      bboxes: list of bounding boxes; each box is a list of integers;  bbox集合
          specifying [xmin, ymin, xmax, ymax]. All boxes are assumed to belong
          to the same label as the image label.
      shape: 3 integers, image shapes in pixels.                   以像素为单位的图片形状
    Returns:
      Example proto     样本原型
    """
    xmin = []
    ymin = []
    xmax = []
    ymax = []
    for b in bboxes:    #将bbox的值以元组的方式进行打包进以上四个列表中
        assert len(b) == 4
        # pylint: disable=expression-not-assigned
        [l.append(point) for l, point in zip([ymin, xmin, ymax, xmax], b)]
        # pylint: enable=expression-not-assigned

    image_format = b'JPEG'
    example = tf.train.Example(features=tf.train.Features(feature={
            'image/height': int64_feature(shape[0]),
            'image/width': int64_feature(shape[1]),
            'image/channels': int64_feature(shape[2]),
            'image/shape': int64_feature(shape),
            'image/object/bbox/xmin': float_feature(xmin),
            'image/object/bbox/xmax': float_feature(xmax),
            'image/object/bbox/ymin': float_feature(ymin),
            'image/object/bbox/ymax': float_feature(ymax),
            'image/object/bbox/label': int64_feature(labels),
            'image/object/bbox/label_text': bytes_feature(labels_text),
            'image/object/bbox/difficult': int64_feature(difficult),
            'image/object/bbox/truncated': int64_feature(truncated),
            'image/format': bytes_feature(image_format),
            'image/encoded': bytes_feature(image_data)}))
    return example


def _add_to_tfrecord(dataset_dir, name, tfrecord_writer):
    """Loads data from image and annotations files and add them to a TFRecord.   装载图片和注释文件并且将他们转换成TFRecord文件

    Args:
      dataset_dir: Dataset directory;               数据集的目录
      name: Image name to add to the TFRecord;      加入到TFRecord中的图片名字
      tfrecord_writer: The TFRecord writer to use for writing.   对于写入的TFRecord的写入流
    """
    image_data, shape, bboxes, labels, labels_text, difficult, truncated = \
        _process_image(dataset_dir, name)                                                #对于每张图片进行处理
    example = _convert_to_example(image_data, labels, labels_text,
                                  bboxes, shape, difficult, truncated)                  #对于每张图片进行原型化
    tfrecord_writer.write(example.SerializeToString())                                  #将原型转换成字符串写入


def _get_output_filename(output_dir, name, idx):
    return '%s\\%s_%03d.tfrecord' % (output_dir, name, idx)


def run(dataset_dir, output_dir, name='voc_train', shuffling=False):
    """Runs the conversion operation.   运行转换操作

    Args:
      dataset_dir: The dataset directory where the dataset is stored.   数据集目录
      output_dir: Output directory.                                     数据输出目录
    """
    if not tf.gfile.Exists(dataset_dir):               #对于这个数据集目录如果不存在，则进行创建目录
        tf.gfile.MakeDirs(dataset_dir)

    # Dataset filenames, and shuffling.             数据集的文件名， 和 打乱
    path = os.path.join(dataset_dir, DIRECTORY_ANNOTATIONS)
    print("path: ", path)
    filenames = sorted(os.listdir(path))             #获得排序后的文件名集合
    if shuffling:                                    #是否要进行混乱抽取，默认否
        random.seed(RANDOM_SEED)
        random.shuffle(filenames)

    # Process dataset files.                 处理数据集文件
    i = 0
    fidx = 0
    while i < len(filenames):
        # Open new TFRecord file.             打开一个新的TFRecord文件
        tf_filename = _get_output_filename(output_dir, name, fidx)
        print("tf_filename :", tf_filename)
        with tf.python_io.TFRecordWriter(tf_filename) as tfrecord_writer:
            j = 0
            while i < len(filenames) and j < SAMPLES_PER_FILES:
                sys.stdout.write('\r>> Converting image %d/%d' % (i+1, len(filenames)))
                sys.stdout.flush()

                filename = filenames[i]
                img_name = filename[:-4]     #获取文件名
                _add_to_tfrecord(dataset_dir, img_name, tfrecord_writer)
                i += 1
                j += 1
            fidx += 1                        #做新的TFRecord文件

    # Finally, write the labels file:
    # labels_to_class_names = dict(zip(range(len(_CLASS_NAMES)), _CLASS_NAMES))
    # dataset_utils.write_label_file(labels_to_class_names, dataset_dir)
    print('\nFinished converting the Pascal VOC dataset!')
