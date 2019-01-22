#import numpy as np
import cv2

#cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out=cv2.VideoWriter("test1.mp4",0, 1, (640,480))
for i in range (1,9200):
    img = cv2.imread(str(i) + ".jpg")
    if(not(img is None)):
        frame = img

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

"""while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
"""
# Release everything if job is finished
#cap.release()
out.release()
cv2.destroyAllWindows()
