import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("sample_video.mp4")
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

#initaiating count variable
count=0;
player_val=True;
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  if ret == True:
      cv2.imshow('Frame',frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.imwrite("frame%d.jpg" % count, frame)
          count+=1;
     
        #press p to ause and play

  # Break the loop
  else: 
     break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
