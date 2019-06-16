#origin dataset
fer2013 = {
    'inpath': '',
    'outpath': '',
}

# dataset
num_readers = 4  # 4个平行的读取器
dataset_name = 'fer2013'
dataset_split_name = 'train'
dataset_dir = ""

# 选择模型model
model_name = 'xception'
dropout_keep_prob = 0.5

# 选择预处理器preprocess
preprocessing_name = 'xception'

# gpu与批处理
gpu_memory_fraction = 0.8 # 动态分配显存
num_preprocessing_threads = 4 # 创建不同线程进行预处理喂数据，因此>1时得到的结果顺序不一致

# train
batch_size = 8
max_number_of_steps = 5000
moving_average_decay = None

# 学习率
learning_rate = 0.01
learning_rate_decay_type = 'exponential' # Specifies how the learning rate is decayed. One of "fixed", "exponential","polynomial".
num_epochs_per_decay = 2.0
learning_rate_decay_factor = 0.94

# 优化器
optimizer = 'adam'   # The name of the optimizer, one of "adadelta", "adagrad", "adam","ftrl", "momentum", "sgd" or "rmsprop".
adadelta_rho = 0.95
adagrad_initial_accumulator_value = 0.1
adam_beta1 = 0.9
adam_beta2 = 0.999
opt_epsilon = 1.0
ftrl_learning_rate_power = -0.5
ftrl_initial_accumulator_value = 0.1
ftrl_l1 = 0.0
ftrl_l2 = 0.0
momentum = 0.9
rmsprop_momentum = 0.9
rmsprop_decay = 0.9

# saver
save_interval_secs = 600

# summary
save_summaries_secs = 60

# log
train_dir = '../logs/ssd_300_vgg_3'
log_every_n_steps = 10
checkpoint_path = None
ignore_missing_vars = False
checkpoint_model_scope = None