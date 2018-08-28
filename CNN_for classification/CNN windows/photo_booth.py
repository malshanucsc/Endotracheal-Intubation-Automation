# USAGE
# python photo_booth.py --output output

# import the necessary packages
from __future__ import print_function
from pyimagesearch.photoboothapp import PhotoBoothApp
from imutils.video import FileVideoStream
import argparse
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="/output",help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
#vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
vs = FileVideoStream("E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/sample_video.mp4").start()
#time.sleep(2.0)

# start the app
pba = PhotoBoothApp(vs, args["output"])
pba.root.mainloop()
