import numpy as np
import cv2

#CONFIG
classToCapture = 'left' #left, right, or idle
desired = 500 # Total images to capture, 80/20 training/testing split
#============

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

capture_counter = 0
frame_counter = 0
while(True):
    frame_counter += 1
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    """
    #If at 30 FPS, this is 2 captures a second
    if frame_counter % 15 == 0:
        frame_counter = 0
        capture_counter += 1
        if capture_counter <= .8 * desired:
            cv2.imwrite('./data/train/' + classToCapture + '/' + classToCapture + str(capture_counter) +'.png', gray)
        else:
            cv2.imwrite('./data/test/' + classToCapture + '/' + classToCapture + str(capture_counter) +'.png', gray)
    """
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # perform inverse binary thresholding 
    (t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

    # make a mask suitable for color images
    mask = cv2.merge([maskLayer, maskLayer, maskLayer])

    # display the mask image
    cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    # use the mask to select the "interesting" part of the image
    sel = cv2.bitwise_and(img, mask)

    # display the result
    cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
    cv2.imshow("selected", sel)
    cv2.waitKey(0)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()