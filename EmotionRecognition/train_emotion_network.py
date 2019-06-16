import tensorflow as tf
import config
import tf_utils
from datasets import dataset_factory
from nets import nets_factory
from preprocessing import preprocessing_factory

slim = tf.contrib.slim


def main():

    # 打印tf日志
    tf.logging.set_verbosity(tf.logging.DEBUG)

    # 建立生成默认计算图上下文
    with tf.Graph().as_default():

        # 选择相应的数据集
        dataset = dataset_factory.get_dataset(
            config.dataset_name, config.dataset_split_name, config.dataset_dir)
        data_provider = slim.dataset_data_provider.DatasetDataProvider(
            dataset, num_readers=config.num_readers, common_queue_capacity=20*config.batch_size, common_queue_min=10*config.batch_size, shuffle=True)
        image_raw, label = data_provider.get(['image', 'label'])

        # 选择模型
        model = nets_factory.get_network_fn(config.model_name, 7, is_training=True, dropout_keep_prob=config.dropout_keep_prob)

        # 选择预处理器
        preprocessing_name = config.preprocessing_name
        image_preprocessing_fn = preprocessing_factory.get_preprocessing(
            preprocessing_name, is_training=True)

        with tf.device('/gpu:0'):

            #建立全局步数
            global_step = slim.create_global_step()

            # 预处理
            image = image_preprocessing_fn(image_raw, 299, 299)

            # 喂入数据
            images, images_raws, labels = tf.train.batch(
                [image, image_raw, label],
                batch_size=config.batch_size,
                num_threads=config.num_preprocessing_threads,
                capacity=5 * config.batch_size)

            # 加载模型
            logits, end_points = model(images, num_classes=dataset.num_classes, is_training=True)
            # 打印模型信息
            for k, v in end_points.items():
                print('name = {}, shape = {}'.format(v.name, v.get_shape()))
            # 打印模型参数
            print("\n")
            print("Parameters")
            for v in slim.get_model_variables():
                print('name = {}, shape = {}'.format(v.name, v.get_shape()))

            # 损失函数
            slim.losses.softmax_cross_entropy(logits, labels)
            total_loss = slim.losses.get_total_loss()

            # 收集摘要
            summaries = set(tf.get_collection(tf.GraphKeys.SUMMARIES))
            for end_point in end_points:
                x = end_points[end_point]
                summaries.add(tf.summary.histogram('activations/' + end_point, x))
                summaries.add(tf.summary.scalar('sparsity/' + end_point,
                                                tf.nn.zero_fraction(x)))
            summaries.add(tf.summary.scalar('total_loss', total_loss))
            for variable in slim.get_model_variables():
                summaries.add(tf.summary.histogram(variable.op.name, variable))

            # 优化器
            learning_rate = tf_utils.configure_learning_rate(config,
                                                             dataset.num_samples,
                                                             global_step)
            optimizer = tf_utils.configure_optimizer(config, learning_rate)
            summaries.add(tf.summary.scalar('learning_rate', learning_rate))

            # 摘要合并.
            summary_op = tf.summary.merge(list(summaries), name='summary_op')

            # 训练步骤
            train_op = slim.learning.create_train_op(total_loss, optimizer)

            # gpu配置
            gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=config.gpu_memory_fraction)
            gpu_config = tf.ConfigProto(log_device_placement=False, allow_soft_placement=True,gpu_options=gpu_options)

            # 断点续训，存储器
            saver = tf.train.Saver(max_to_keep=5,
                                   keep_checkpoint_every_n_hours=1.0,
                                   write_version=2,
                                   pad_step_number=False)

            # 训练
            final_loss = slim.learning.train(
                train_op,
                logdir=config.train_dir,
                init_fn=tf_utils.get_init_fn(config),
                summary_op=summary_op,
                number_of_steps=config.max_number_of_steps,
                log_every_n_steps=config.log_every_n_steps,
                save_summaries_secs=config.save_summaries_secs,
                saver=saver,
                save_interval_secs=config.save_interval_secs,
                session_config=gpu_config,
                sync_optimizer=None)

    print("Finished training. Last batch loss:", final_loss)
    print("Checkpoint saved in %s" % config.train_dir)


if __name__ == '__main__':
    main()
