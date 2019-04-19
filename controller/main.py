import numpy as np
from keras.models import load_model
from PIL import Image
from skimage import transform
import cv2
from os.path import realpath, normpath
from pynput.keyboard import Key, Controller
from subprocess import Popen

model = load_model('../classifier/model.h5')
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

    if counter % 5 == 0:
        counter = 0

        height, width, channels =  img.shape
        #Crop out person and merge together hands
        left = img[int(height * .25): height, 0 : int(width / 3)]
        right = img[int(height * .25): height, width - int(width / 3) : width]
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
     
    

    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 