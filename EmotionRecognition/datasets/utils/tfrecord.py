# coding=utf-8
import tensorflow as tf
import numpy as np
import os
from PIL import Image

slim = tf.contrib.slim


# 创建TFrecord文件
def create_record_file():
    train_filename = "train.tfrecords"
    if os.path.exists(train_filename):
        os.remove(train_filename)

    # 创建.tfrecord文件，准备写入
    writer = tf.python_io.TFRecordWriter('./' + train_filename)
    with tf.Session() as sess:
        for i in range(10):
            img_raw = tf.gfile.FastGFile("D:/test/" + str(i) + ".jpg", 'rb').read()
            decode_data = tf.image.decode_jpeg(img_raw)
            image_shape = decode_data.eval().shape
            example = tf.train.Example(features=tf.train.Features(
                feature={
                    'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
                    'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=[b'jpg'])),
                    'image/width': tf.train.Feature(int64_list=tf.train.Int64List(value=[image_shape[1]])),
                    'image/height': tf.train.Feature(int64_list=tf.train.Int64List(value=[image_shape[0]])),
                    'image/label': tf.train.Feature(int64_list=tf.train.Int64List(value=[i])),
                }))
            writer.write(example.SerializeToString())  # 序列化保存
        writer.close()
        print("保存tfrecord文件成功。")


# 使用Slim的方法从TFrecord文件中读取
def read_record_file():
    tfrecords_filename = "train.tfrecords"
    # 将tf.train.Example反序列化成存储之前的格式。由tf完成
    keys_to_features = {
        'image/encoded': tf.FixedLenFeature((), tf.string, default_value=''),
        'image/format': tf.FixedLenFeature((), tf.string, default_value='jpeg'),
        'image/width': tf.FixedLenFeature((), tf.int64, default_value=0),
        'image/height': tf.FixedLenFeature((), tf.int64, default_value=0),
        'image/label': tf.FixedLenFeature((), tf.int64, default_value=0),
    }
    # 将反序列化的数据组装成更高级的格式。由slim完成
    items_to_handlers = {
        'image': slim.tfexample_decoder.Image(image_key='image/encoded',
                                              format_key='image/format',
                                              channels=3),
        'label': slim.tfexample_decoder.Tensor('image/label'),
        'height': slim.tfexample_decoder.Tensor('image/height'),
        'width': slim.tfexample_decoder.Tensor('image/width')
    }
    # 定义解码器，进行解码
    decoder = slim.tfexample_decoder.TFExampleDecoder(keys_to_features, items_to_handlers)
    # 定义dataset，该对象定义了数据集的文件位置，解码方式等元信息
    dataset = slim.dataset.Dataset(
        data_sources=tfrecords_filename,
        reader=tf.TFRecordReader,
        decoder=decoder,
        num_samples=10,  # 训练数据的总数
        items_to_descriptions=None,
        num_classes=10,
    )
    # 使用provider对象根据dataset信息读取数据
    provider = slim.dataset_data_provider.DatasetDataProvider(
        dataset,
        num_readers=1,
        common_queue_capacity=20,
        common_queue_min=1)

    # 获取数据
    [image, label, height, width] = provider.get(['image', 'label', 'height', 'width'])
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        for i in range(10):
            img, l, h, w = sess.run([image, label, height, width])
            img = tf.reshape(img, [h, w, 3])
            print(img.shape)
            img = Image.fromarray(img.eval(), 'RGB')  # 这里将narray转为Image类，Image转narray：a=np.array(img)
            img.save('./' + str(l) + '.jpg')  # 保存图片

        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    create_record_file()
    read_record_file()