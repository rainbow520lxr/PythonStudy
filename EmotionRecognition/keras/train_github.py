"""
File: train_emotion_classifier.py
Author: Octavio Arriaga
Email: arriaga.camargo@gmail.com
Github: https://github.com/oarriaga
Description: Train emotion classification model
"""

from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
from keras.callbacks import LearningRateScheduler
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import xception
from keras import optimizers
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF

from keras.models_github import *


config = tf.ConfigProto()
config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
sess = tf.Session(config=config)

KTF.set_session(sess)

# parameters
batch_size = 64
num_epochs = 10000
input_shape = (64, 64, 3)
validation_split = .2
verbose = 1
num_classes = 7
patience = 50
train_dir = '/home/xqy/datasets/emotion/newaffectnet_data/train'
validation_dir = '/home/xqy/datasets/emotion/newaffectnet_data/val'

# data generator
train_datagen = ImageDataGenerator(
    featurewise_center=False,
    featurewise_std_normalization=False,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=.1,
    horizontal_flip=True,
    preprocessing_function=xception.preprocess_input)


validation_datagen = ImageDataGenerator(preprocessing_function=xception.preprocess_input)

train_generator = train_datagen.flow_from_directory(train_dir, target_size=(64, 64),
                                                    color_mode="rgb", batch_size=batch_size)

validataion_generator = validation_datagen.flow_from_directory(validation_dir, target_size=(64, 64),
                                                               color_mode="rgb", batch_size=batch_size)

# model parameters/compilation
momentum_lr = 0.003
lr_decay = 0.95
decay_per_epoch = 10

model = mini_XCEPTION(input_shape, num_classes)
opt= optimizers.SGD(momentum_lr,0.9,1e-6, nesterov=True)
# opt= optimizers.Adam(0.01)
model.compile(optimizer=opt, loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()




# 学习率每两轮乘0.95
def learning_decay(epoch):
    return momentum_lr * (lr_decay ** (epoch // decay_per_epoch))

reduce_lr = LearningRateScheduler(learning_decay)

log_file_path = './log/_emotion_training.log'
csv_logger = CSVLogger(log_file_path, append=False)
early_stop = EarlyStopping('val_loss', patience=patience)
# reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1,
#                               patience=int(patience / 4), verbose=1)
trained_models_path ='./model/mini_XCEPTION'
model_names = trained_models_path + '.{epoch:02d}-{val_acc:.2f}.hdf5'
model_checkpoint = ModelCheckpoint(model_names, 'val_loss', verbose=1,
                                   save_best_only=True)
callbacks = [model_checkpoint, csv_logger, early_stop, reduce_lr]

model.fit_generator(train_generator,
                    steps_per_epoch=len(train_generator),
                    epochs=num_epochs, verbose=2, callbacks=callbacks,
                    validation_data=validataion_generator,validation_steps=len(validataion_generator))
