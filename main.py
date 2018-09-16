import numpy as np
import cv2


def create_element(dilatation_type,dilatation_size):
    return cv2.getStructuringElement(dilatation_type, (2*dilatation_size + 1, 2*dilatation_size+1), (dilatation_size, dilatation_size))
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

ret, previous_frame = cap.read()
display = previous_frame
fgbg = cv2.createBackgroundSubtractorMOG2()

learning_rate = 0.1

for i in range(100):
    ret, frame = cap.read()
    fgbg.apply(frame,learning_rate)
learning_rate = 0.001
while(True):
    
    ret, frame = cap.read()
 
    fgmask = fgbg.apply(frame,learning_rate)
    ret, fgmask = cv2.threshold(fgmask, 200,255,cv2.THRESH_BINARY)

    # Erode
    dilatation_type = cv2.MORPH_ELLIPSE
    element = create_element(dilatation_type,2)
    element2 = create_element(dilatation_type,5)

    #fgmask = cv2.erode(fgmask,element,iterations =1 )
    opening = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,element)
    fgmask = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,element2)
    #fgmask = cv2.dilate(fgmask,element,iterations =1 )
    bgmask = cv2.bitwise_not(fgmask)

    fg = cv2.bitwise_and(frame,frame,mask = fgmask)
    bg = cv2.bitwise_and(display,display,mask =bgmask)
    display = cv2.add(fg ,bg )

    #cv2.imshow('orginal',fgbg.getBackgroundImage())
    #cv2.imshow('opening',opening)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('window',display)
    #cv2.imshow('mask',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
