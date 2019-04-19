
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, Callback
from skimage import exposure
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import clear_output
#CONFIG=======
batch_size= 10
image_width = 213
image_height = 180
#=============

class PlotLearning(Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.acc = []
        self.val_acc = []
        self.fig = plt.figure()
        
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.acc.append(logs.get('acc'))
        self.val_acc.append(logs.get('val_acc'))
        self.i += 1
        f, (ax1, ax2) = plt.subplots(1, 2, sharex=True)
        
        clear_output(wait=True)
        
        ax1.set_yscale('log')
        ax1.plot(self.x, self.losses, label="loss")
        ax1.plot(self.x, self.val_losses, label="val_loss")
        ax1.legend()
        
        ax2.plot(self.x, self.acc, label="accuracy")
        ax2.plot(self.x, self.val_acc, label="validation accuracy")
        ax2.legend()
        
        plt.show();
        
plot = PlotLearning()

checkpoint = ModelCheckpoint('./model.h5', monitor='val_acc', verbose=1, save_best_only=False, mode='max')
callbacks_list = [checkpoint, plot]

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
    rotation_range=3,
    width_shift_range=.1, 
    height_shift_range=.1,
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
    shuffle=True,
    color_mode='grayscale',
    class_mode='binary'
)
val_generator = val_datagen.flow_from_directory(
    val_data_dir,
    target_size=(image_width, image_height),
    batch_size=batch_size,
    shuffle=True,
    color_mode='grayscale',
    class_mode='binary'
)

model.fit_generator(
    train_generator,
    epochs=50,
    shuffle=True,
    callbacks=callbacks_list,
    validation_data=val_generator,
)