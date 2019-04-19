import numpy as np
from keras.models import load_model
from PIL import Image
from skimage import transform
import cv2
from os.path import realpath, normpath
from pynput.keyboard import Key, Controller

# Load the Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
goggles = cv2.imread('../assets/goggles.png', -1)

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src

def drawMask(gray):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x,y,w,h) in faces: 
        if h > 0 and w > 0:
            glass_symin = int(y - 10 )
            glass_symax = int(y + h - 10)
            sh_glass = glass_symax - glass_symin
            face_glass_roi_color = img[glass_symin:glass_symax, x:x+w]
            goggles_r = cv2.resize(goggles, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
            transparentOverlay(face_glass_roi_color,goggles_r)