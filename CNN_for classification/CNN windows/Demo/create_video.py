import cv2
import glob
format="XVID"
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#fourcc = VideoWriter_fourcc(*format)
#fourcc = cv2.VideoWriter_fourcc(*'mp4')
video=cv2.VideoWriter('Demo.avi',cv2.VideoWriter_fourcc(*'DIVX'),20.0,(720,645))
for i in range(1,934):
    img = cv2.imread(str(i)+".jpg")
    video.write(img)
video.release()