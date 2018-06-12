import cv2
import numpy as np
start_time_minute=int(input("start minute :  "));
start_time_second=int(input("start second :  "));

end_time_minute=int(input("end minute :  "));
end_time_second=int(input("end second :  "));

start_time=(start_time_minute*60) + start_time_second
end_time=(end_time_minute*60) + end_time_second

flag1=False;
flag2=False;
cap = cv2.VideoCapture("sample_video.mp4")
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  exit()


count=0;
print("please Wait !!!");
# Read until video is completed
while(cap.isOpened()):
  

    
  # Capture frame-by-frame
  ret, frame = cap.read()
  
  fps = cap.get(cv2.CAP_PROP_FPS)
  
  
  videotime = count / fps
  count+=1;

  if ret == True:
      if(videotime>=start_time and videotime<=end_time):
        flag1=True;
        flag2=False;
        cv2.imshow('Frame',frame)
        cv2.imwrite("Output_images/frame%d.jpg" % count, frame)
      else:
        flag2=True;
      if cv2.waitKey(25) & 0xFF == ord('q'):
          break;
      

      if(flag1==True and flag2==True):
        break;


  # Break the loop
  else: 
     break
print("check the output folder !!")
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()








