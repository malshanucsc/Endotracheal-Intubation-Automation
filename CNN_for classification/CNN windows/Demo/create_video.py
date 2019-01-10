import cv2
import glob
format="XVID"
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#fourcc = VideoWriter_fourcc(*format)
#fourcc = cv2.VideoWriter_fourcc(*'mp4')
img = cv2.imread("1.jpg")
h,w,g=img.shape
#video=cv2.VideoWriter('Demo.avi',cv2.VideoWriter_fourcc(*'DIVX'),20.0,(720,645))
video=cv2.VideoWriter('Demo.avi',cv2.VideoWriter_fourcc(*'DIVX'),20.0,(w,h))
#array2=["frame1_","frame2_","frame3_","frame5_","frame6_","frame7_","frame8_"]
#video = cv2.VideoWriter('video.avi',0,1,(w,h))
#j=1

for i in range (1,9200):
    img = cv2.imread("newdemo/"+str(i)+".jpg")
    if(not(img is None)):
        #h,w,g=img.shape

        #print(i)
        cv2.imshow("Demo",img)
        #j+=1
        cv2.waitKey(100)
        #video.write(img)

"""
for filename in glob.glob("newdemo/newestimages/*.jpg"):
    
    img = cv2.imread(filename)
    print(filename)
    cv2.imshow("im",img)
    video.write(img)

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
"""
cv2.destroyAllWindows()
video.release()
