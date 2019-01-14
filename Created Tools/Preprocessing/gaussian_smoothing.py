import cv2
import numpy as np
count i=0
for filename in glob.glob('*.jpg'):
    img = cv2.imread('path to the image')
    blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite(str(i)+'.jpg', blur)

