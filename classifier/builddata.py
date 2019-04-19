import numpy as np
import cv2

#CONFIG
classToCapture = 'right' #left, right, or idle
desired = 600 # Total images to capture, 80/20 training/testing split

#============

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

capture_counter = 0
frame_counter = 0
while(True):
    if (capture_counter == desired):
        break

    frame_counter += 1
    # Capture frame-by-frame
    ret, frame = cap.read()

    
    #If at 30 FPS, this is 3 captures a second
    if frame_counter % 5 == 0:
        frame_counter = 0
        capture_counter += 1
        height, width, channels =  frame.shape
        
        #Crop out person and merge together hands
        left = frame[int(height * .25): height, 0 : int(width / 3)]
        right = frame[int(height * .25): height, width - int(width / 3) : width]
        hands = np.concatenate((left, right), axis=1)

        #Blur and threshold 
        gray = cv2.cvtColor(hands, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),2)   
        th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        if capture_counter <= .7 * desired:
            cv2.imwrite('./data/train/' + classToCapture + '/' + classToCapture + str(capture_counter) +'.png', res)
        else:
            cv2.imwrite('./data/test/' + classToCapture + '/' + classToCapture + str(capture_counter) +'.png', res)
        print('Captured ' + str(capture_counter))
    
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()