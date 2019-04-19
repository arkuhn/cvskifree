
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint
from skimage import exposure
import numpy as np


#CONFIG=======
batch_size= 14
image_width = 320
image_height = 240
#=============


checkpoint = ModelCheckpoint('./model.h5', monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

train_data_dir = './data/train/'
val_data_dir = './data/val/'


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(image_width, image_height, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.6))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

#Train and val data augmentors
train_datagen = ImageDataGenerator (
    rescale=1./255,
    rotation_range=10,
    width_shift_range=.2, 
    height_shift_range=.2,
    fill_mode='nearest'
)
val_datagen = ImageDataGenerator(
    rescale=1./255,
    fill_mode='nearest'
)

#Generators for TRAIN and val
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(image_width, image_height),
    batch_size=batch_size,
    color_mode='grayscale',
    shuffle=True,
    class_mode='binary'
)
val_generator = val_datagen.flow_from_directory(
    val_data_dir,
    target_size=(image_width, image_height),
    batch_size=batch_size,
    color_mode='grayscale',
    shuffle=True,
    class_mode='binary'
)

model.fit_generator(
    train_generator,
    steps_per_epoch= 1600 // batch_size,
    epochs=10,
    shuffle=True,
    callbacks=callbacks_list,
    validation_data=val_generator,
    validation_steps= 400 // batch_size 
)