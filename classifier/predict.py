from keras.models import load_model
import numpy as np
from PIL import Image
from skimage import transform


model = load_model('model.h5')

np_image = Image.open('left1.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')

np_image = Image.open('left2.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')

np_image = Image.open('left3.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')

np_image = Image.open('right1.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')

np_image = Image.open('right2.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')


np_image = Image.open('right3.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (213, 180, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('right')
else:
    print('left')


