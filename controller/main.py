import numpy as np
from keras.models import load_model
from PIL import Image
from skimage import transform
import cv2
from os.path import realpath, normpath
from pynput.keyboard import Key, Controller
from subprocess import Popen

model = load_model('../classifier/1-78-model.h5')
keyboard = Controller()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
process = Popen(['python', '../game/main.py'], shell=True,
             stdin=None, stdout=None, stderr=None)
counter = 0
moving = 'left'
while 1: 
    counter += 1
    ret, img = cap.read() 
   
    cv2.putText(img,'CVSkiFree',(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
    height, width, channels =  img.shape
    y0 = int(height * .25)
    y1 = height
    left_x0 = 0
    left_x1 = int(width / 3)
    right_x0 =  width - int(width / 3)
    right_x1 = width
    if counter % 10 == 0:
        counter = 0

        height, width, channels =  img.shape
        #Crop out person and merge together hands
        left = img[y0: y1, left_x0 : left_x1]
        right = img[y0: y1, right_x0 : right_x1]
        hands = np.concatenate((left, right), axis=1)

        #Blur and threshold 
        gray = cv2.cvtColor(hands, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),2)   
        th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        np_image = np.array(res).astype('float32')/255
        np_image = transform.resize(np_image, (213, 180, 1))
        np_image = np.expand_dims(np_image, axis=0)
        result = model.predict(np_image)
        if result[0][0] >= 0.5:
            print('right')
            keyboard.press('d')
            keyboard.release('d')
        else:
            print('left')
            keyboard.press('a')
            keyboard.release('a')
     
    dst = img.copy()
    dst = cv2.flip(img, 1);
    height, width, channels =  dst.shape
    cv2.rectangle(dst, (left_x0, y0), (left_x1, y1),  (255,0,0), 2)
    cv2.rectangle(dst, (right_x0, y0), (right_x1, y1),  (255,0,0), 2)
    cv2.imshow('img', dst) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 