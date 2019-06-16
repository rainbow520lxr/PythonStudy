from keras.applications import *
from keras.layers import *
from keras.models import *
from keras.callbacks import LearningRateScheduler, ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras import regularizers
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
#
# model = Sequential()
# model.add(Conv2D(64, (3, 3),strides=(1,1), padding='same', activation='relu', input_shape=(64, 64, 1)))
# model.add(BatchNormalization())
# model.add(Conv2D(128,(3,3), strides=(2,2),padding='same',activation='relu'))
# model.add(BatchNormalization())
# model.add(MaxPool2D(strides=2))
# model.add(Conv2D(128, (3,3), strides=(1,1),activation='relu'))
# model.add(BatchNormalization())
# model.add(Conv2D(128, (3,3), strides=(2,2),activation='relu'))
# model.add(BatchNormalization())
# model.add(AveragePooling2D(strides=2))
# model.add(Flatten())
# model.add(Dense(1000, activation="relu"))
# model.add(Dropout(0.5))
# model.add(Dense(7, activation="softmax"))

config = tf.ConfigProto()
config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
sess = tf.Session(config=config)

KTF.set_session(sess)

def simple_CNN(input_shape, num_classes):

    model = Sequential()
    model.add(Convolution2D(filters=16, kernel_size=(7, 7), padding='same',
                            name='image_array', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters=16, kernel_size=(7, 7), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(.5))

    model.add(Convolution2D(filters=32, kernel_size=(5, 5), padding='same'))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters=32, kernel_size=(5, 5), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(.5))

    model.add(Convolution2D(filters=64, kernel_size=(3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters=64, kernel_size=(3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(.5))

    model.add(Convolution2D(filters=128, kernel_size=(3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters=128, kernel_size=(3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(AveragePooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(.5))

    model.add(Convolution2D(filters=256, kernel_size=(3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=num_classes, kernel_size=(3, 3), padding='same'))
    model.add(GlobalAveragePooling2D())
    model.add(Activation('softmax', name='predictions'))
    return model

model = simple_CNN((48,48,3),7)


model.summary()


train_dir = '/home/xqy/datasets/emotion/newaffectnet_data/train'
validation_dir = '/home/xqy/datasets/emotion/newaffectnet_data/val'

train_datagen = ImageDataGenerator(rotation_range=10,
                                   zoom_range=0.1, preprocessing_function=xception.preprocess_input)

validation_datagen = ImageDataGenerator(preprocessing_function=xception.preprocess_input)

train_generator = train_datagen.flow_from_directory(train_dir, target_size=(48, 48),
                                                    color_mode="rgb", batch_size=4)

validataion_generator = validation_datagen.flow_from_directory(validation_dir, target_size=(48, 48),
                                                               color_mode="rgb",batch_size=4)

# opt = optimizers.Adam(0.01)
opt = optimizers.SGD(0.01,0.9, 1e-6, nesterov=True)
model.compile(opt, "categorical_crossentropy", ["accuracy"])
model.fit_generator(train_generator, epochs=500, steps_per_epoch=28709/128,validation_steps=3589/128,
                    validation_data=validataion_generator, verbose=2)
