import cv2
import glob
format="XVID"
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#fourcc = VideoWriter_fourcc(*format)
#fourcc = cv2.VideoWriter_fourcc(*'mp4')
video=cv2.VideoWriter('Demo.avi',cv2.VideoWriter_fourcc(*'DIVX'),20.0,(720,645))
array2=["frame1_","frame2_","frame3_","frame5_","frame6_","frame7_","frame8_"]
for i in array2:
    if(i=="frame1_"):
        for j in range(1,645):
            filename="frame1_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame2_"):
        for j in range(1, 645):
            filename = "frame2_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame3_"):
        for j in range(1, 646):
            filename = "frame3_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame5_"):
        for j in range(1, 645):
            filename = "frame5_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame6_"):
        for j in range(1, 645):
            filename = "frame6_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame7_"):
        for j in range(1, 645):
            filename = "frame1_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)

    if (i == "frame8_"):
        for j in range(1, 921):
            filename = "frame8_"+str(j)+".jpg"
            img = cv2.imread(filename)
            video.write(img)


video.release()
