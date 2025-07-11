import numpy as np
import cv2

from PIL import Image

from util import get_limits

yellow = [0, 255, 255] # yellow in bgr colorspace and pink(203,192,255)
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        # print(frame.shape)
        cv2.putText(frame,"yellow",(x1 + (x2//2)  , y1 + (y2//2)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

    # print(bbox)

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


#  cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3) # img, text , origin , fontFace , fontScale , color , thickness= none, lineType = none, bottomLeftOrigin = None

