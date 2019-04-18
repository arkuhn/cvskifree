from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from sklearn.metrics import classification_report
from keras.models import load_model
import numpy as np
import sys, os
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator, image
from keras.callbacks import ModelCheckpoint

model = load_model('model.h5')

test_image  = image.load_img('left.jpg', target_size=(120, 320), color_mode='grayscale')
test_image = img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('left')
else:
    print('right')



test_image  = image.load_img('right.jpg', target_size=(120, 320), color_mode='grayscale')
test_image = img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('left')
else:
    print('right')