from keras.models import load_model
import numpy as np
from PIL import Image
from skimage import transform


model = load_model('model.h5')

np_image = Image.open('left.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (320, 240, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('left')
else:
    print('right')

np_image = Image.open('right.png')
np_image = np.array(np_image).astype('float32')/255
np_image = transform.resize(np_image, (320, 240, 1))
np_image = np.expand_dims(np_image, axis=0)
result = model.predict(np_image)
print(str(result[0][0]))
if result[0][0] >= 0.5:
    print('left')
else:
    print('right')

