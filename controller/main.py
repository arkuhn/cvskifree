import numpy as np
from keras.models import load_model
from PIL import Image
from skimage import transform
import cv2
from os.path import realpath, normpath
from pynput.keyboard import Key, Controller

model = load_model('../classifier/model.h5')
keyboard = Controller()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)


counter = 0
moving = 'left'
while 1: 
    counter += 1
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    cv2.putText(img,'CVSkiFree',(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)

    if counter % 10 == 0:
        counter = 0
        np_image = np.array(gray).astype('float32')/255
        np_image = transform.resize(np_image, (320, 240, 1))
        np_image = np.expand_dims(np_image, axis=0)
        result = model.predict(np_image)
        if result[0][0] >= 0.5:
            print('left')
            keyboard.press('a')
            keyboard.release('a')
        else:
            print('right')
            keyboard.press('d')
            keyboard.release('d')
    

    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 