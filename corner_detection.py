import cv2 as cv
import numpy as np
import sys

video = cv.VideoCapture(0)

if not video.isOpened():
    sys.exit("unable to detect camera")

while True:
    
    __, frame = video.read()
    
    cvt = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    edge = cv.goodFeaturesToTrack(cvt, 8, 0.01, 10)
    
    coners = np.int32(edge)
    
    for lines in coners:
        x,y = lines.ravel()
        
        cv.circle(frame, (x,y), 5, (0,0,255), -1)
        
    cv.imshow("img", frame)
    
    key = cv.waitKey(1)
    
    if key == ord("q"):
        break

cv.destroyAllWindows()
video.release()
