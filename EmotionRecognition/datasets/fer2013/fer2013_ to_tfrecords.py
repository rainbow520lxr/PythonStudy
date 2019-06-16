import os
import tensorflow as tf
from PIL import Image  # 注意Image,后面会用到
import matplotlib.pyplot as plt
import numpy as np
import sys
import config
# 数据集的实际地址
# 文件夹的命名应避开关键词，否则会提示找不到路径
cwd = config.fer2013.inpath
# 人为的将数据设定为六类
classes = {'bo_luo_tai', 'chi_hen', 'dian_ci', 'hou_tai', 'lie_wen', 'zheng_chang'}
output_dir = config.fer2013.outpath
name = 'fer2013_train'

# tf_record参数
SAMPLES_PER_FILES = 200
# --------------------------------------------把数据存储为TFRrcord格式--------------------------------------------------#
'''
注意： 
 "label"和'img_raw'的名称和数据类型在生成TFRecord代码和将TFRecord读出时的代码一样
'''


def _convert_to_example(index, img_raw):
    """Build an Example proto for an image example.

    Args:
      index: Label
      img_raw: image
    Returns:
      Example proto
    """
    example = tf.train.Example(
        features=tf.train.Features(
            feature={
                'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
                'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=[b'jpg'])),
                "image/label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),  # index 为标签
            }))  # example对象对label和image数据进行封装
    return example


def _add_to_tfrecord(index, img_raw, tfrecord_writer):
    """Loads data from image and annotations files and add them to a TFRecord.

    Args:
      dataset_dir: Dataset directory;
      name: Image name to add to the TFRecord;
      tfrecord_writer: The TFRecord writer to use for writing.
    """
    example = _convert_to_example(index, img_raw)
    tfrecord_writer.write(example.SerializeToString())


def _get_output_filename(output_dir, name, label, idx):
    return '%s/%s_%s_%03d.tfrecord' % (output_dir, name, label, idx)


def main():
    for index, item in enumerate(classes):  # enumerate()可以同时获得索引和元素
        class_path = os.path.join(cwd, item)
        filenames = sorted(os.listdir(class_path))
        i = 0
        fidx = 0
        while i < len(filenames):
            # Open new TFRecord file.
            tf_filename = _get_output_filename(output_dir, name, item, fidx)
            with tf.python_io.TFRecordWriter(tf_filename) as tfrecord_writer:
                j = 0
                while i < len(filenames) and j < SAMPLES_PER_FILES:
                    sys.stdout.write('\r>> Converting image/%s %d/%d' % (item, i + 1, len(filenames)))
                    sys.stdout.flush()

                    img_path = class_path + filenames[i]  # 每一个图片的地址
                    img = Image.open(img_path)
                    img = img.resize((256, 256))  # 图片设置为256*256
                    img_raw = img.tobytes()  # 将每一个图片转化为二进制格式
                    _add_to_tfrecord(index, img_raw, tfrecord_writer)

                    i += 1
                    j += 1
                fidx += 1


if __name__ == '__main__':
    main()
