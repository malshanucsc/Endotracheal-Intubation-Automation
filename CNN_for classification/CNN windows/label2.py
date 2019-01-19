# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import datetime
import numpy as np
import tensorflow as tf
import cv2
import threading
import time
from PIL import Image
import glob
import random
import sys

# import the necessary packages for UI


import tkinter
import Queue

import PIL.Image, PIL.ImageTk

import sys
sys.path.insert(0, 'GUI/')

import manual


##ui end


count = 1


class prediction:
    def load_graph(self, model_file):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(model_file, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)


        return graph

    #def read_tensor_from_image_file(self, img, input_height=299, input_width=299, input_mean=0, input_std=255):

        # print(resized)

        #return result

    def load_labels(self, label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        #print(label)
        return label

    def getNextDirection(self, new_location, movement_type):

        if movement_type == "forward":

            if (new_location == 2 or new_location == 7):
                # bend the  tube downward due to curves in the nasal  cavity and trachea
                return 1
            elif new_location == 4:
                # due to sensitivity in this area tracheal opening close and open quickly.
                #  waiting sometimes there will stabilize the opening
                return 2
            elif new_location == 5:
                # when tracheal openning closed it always tend to close it a obstacle is near the opening
                return 3
            elif new_location == 8:
                # reduce touching with wall of wind pipe spirals to reduce bleedings
                return 4
            elif new_location == 9:
                # if sped is high and miss the location 10 tube will move further and then it is difficult to capture due to locations beyond 10 is similar as 8-10
                return 5
            elif new_location == 10:
                # since intubation tube should stop 2cm above to spread air for both lungs
                return 6
            else:
                return 7

        if movement_type == "backward":
            if (new_location == 2 or new_location == 7):
                # bend the  tube upward due to curves in the nasal  cavity and trachea
                return 8
            else:
                return 9

    #def output_frame_details(self):
        # print(input_height)



    def visualize_func(self, predicting_location ):
        file_name = predicting_location
        if predicting_location == 0:
            file_name = 1
        elif predicting_location == 1:
            file_name = 10
        direction_output = self.getNextDirection(file_name, "forward")
        self.output_location=file_name

        if(direction_output==1):
            self.navigation_message="Move forward with downward thrust"
        elif(direction_output==2):
            self.navigation_message="Wait for few seconds till location 4 is stable"
        elif(direction_output==3):
            self.navigation_message="Stop. Move 1cm back"
        elif(direction_output==4):
            self.navigation_message="Move center pixels towards black hole"
        elif(direction_output==5):
            self.navigation_message="Move forward with extreme slow"
        elif(direction_output==6):
            self.navigation_message="Stop move 2cm back"
        elif(direction_output==7):
            self.navigation_message="Move forward"
        elif(direction_output==8):
            self.navigation_message="Move backward with upward thrust"
        elif(direction_output==9):
            self.navigation_message="Move backward"

        #print(file_name)
        #self.count+=1

        for filename in glob.glob("../surf_images/location" + str(file_name) + "/*.jpg"):


            match_img = cv2.imread(filename, 0)
            # cv2.imshow("matching image",match_img)
            kp1, des1 = self.surf.detectAndCompute(match_img, None)

            # outkeypointimages=cv2.drawKeypoints(match_img, kp1, np.array([]), (0,0,255));
            # cv2.imshow("asas",outkeypointimages)
            # cv2.imwrite("surf_images/keypoints/"+str(random.randint(1,100000))+".jpg",outkeypointimages)

            temp_out_img = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)

            kp2, des2 = self.surf.detectAndCompute(temp_out_img, None)


            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            # bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)

            # matches = bf.match(des1, des2)

            flann = cv2.FlannBasedMatcher(index_params, search_params)

            if des2 is None:
                break
            if len(des2) <= 1:
                break


            matches = flann.knnMatch(des1, des2, k=2)

            # matches = sorted(matches, key=lambda x: x.distance)

            good = []

            for m, n in matches:
                if m.distance < 0.99 * n.distance:
                    good.append(m)
            #print(len(good))

            if len(good) > 20:
                self.first_pointer = True
                src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                M = []

                M, mask = cv2.findHomography(src_pts, dst_pts, 0, 5.0)

                h, w = temp_out_img.shape
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

                # print(type(M))

                if isinstance(M, np.ndarray):
                    self.dst = cv2.perspectiveTransform(pts, M)
                    # img2 = cv2.polylines(self.img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
                    # cv2.imwrite("surf_images/polylines/"+str(random.randint(1,100000))+".jpg",img2)
                    # print(dst)
                    # h2,w2,g=self.img2.shape
                    # print(h2)
                    # print(w2)
                    # print(g)
                    #print(self.dst)
                    self.xx = (self.dst[0][0][0] + self.dst[1][0][0] + self.dst[2][0][0] + self.dst[3][0][0]) / 4
                    self.yy = (self.dst[0][0][1] + self.dst[1][0][1] + self.dst[2][0][1] + self.dst[3][0][1]) / 4
                    if(self.xx > 0 and self.yy > 0):
                        self.x = self.xx
                        self.y = self.yy
                    else:
                        self.x = 240
                        self.y = 213



                    break


        if self.first_pointer == True:
            #print(str(self.x)+"     "+str(self.y))

            hh2, ww2, g = self.img2.shape

            #print(str(hh2)+"  "+str(ww2))

            if self.x < 20:
                self.x += 20
            if self.x > 461:
                self.x -= 20
            if self.y < 20:
                self.y += 20
            if self.y > 406:
                self.y -= 20

            if np.int32(self.y) == 102:
                self.y = 180
            #print(str(self.x) + "     " + str(self.y))


            cv2.circle(self.img2, (np.int32(self.x), np.int32(self.y)), 10, (0, 0, 255), -1)
            #print(np.int32(self.x))

                # cv2.line(self.img2, (dst[0][0][0],dst[0][0][1]), (dst[1][0][0],dst[1][0][1]), (0, 255, 0), 4);
                # cv2.line(self.img2, (dst[1][0][0],dst[1][0][1]), (dst[2][0][0], dst[2][0][1]), (0, 255, 0), 4);
                # cv2.line(self.img2, (dst[2][0][0], dst[2][0][1]), (dst[3][0][0], dst[3][0][1]), (0, 255, 0), 4);
                # cv2.line(self.img2, (dst[3][0][0], dst[3][0][1]), (dst[0][0][0], dst[0][0][1]), (0, 255, 0), 4);

                # line(image, scene_corners[1], scene_corners[2], Scalar(0, 255, 0), 4);

                # line(image, scene_corners[2], scene_corners[3], Scalar(0, 255, 0), 4);

                # line(image, scene_corners[3], scene_corners[0], Scalar(0, 255, 0), 4);

                # self.img2 = cv2.polylines(self.img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
                # h2, w2,g = self.img2.shape
                # print(h2)
                # print(w2)
                # print(g)
        #print(str(self.count) + "   " + str(self.first_pointer))


        new_direction = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/directions/new/" + str(
            direction_output) + ".jpg"

        new_location = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/locations/new2/" + str(
            file_name) + ".jpg"
        if self.location != new_location:
            #self.location_image = cv2.imread(new_location)
            self.location = new_location

        if self.direction != direction_output:
            #self.direction_image = cv2.imread(new_direction)
            self.direction = direction_output

        # print(self.direction_image)
        #vis1 = np.hstack((self.direction_image, self.location_image))
        #vis1 = vis1[0:65, 14:440]

        self.vis = self.img2

        write_name = "surf_images/" + str(self.count) + ".jpg"
        self.count += 1


        #UI part



        #self.update()
        #self.window.update()






        ##ui part end

        #h,w,g=self.vis.shape
        #print(h)
        #print(w)
        self.queue.enqueue(self.vis)


        #cv2.imshow("Prediction", self.vis)
        #cv2.imwrite(write_name, self.vis)
        # time.sleep(0.001)

    def readframe_func(self):
        #r_placeholder = tf.placeholder(tf.float32, shape=[])
        #out_t = tf.trace(tf.random_normal((4, 4), r_placeholder, 1.0))
        #if(running==False):
        #return

        with tf.Session(graph=self.graph) as sess:

            while self.cap.isOpened():
                ret, self.img = self.cap.read()
                # print(self.img)
                self.img2 = self.img[43:524, 146:572]

                self.img = self.img[43:524, 146:572]

                # time.sleep(1)
                cv2.waitKey(1)
                #self.output_frame_details();

                #t = self.read_tensor_from_image_file(self.img,input_height=self.input_height,input_width=self.input_width,input_mean=self.input_mean,input_std=self.input_std)

                input_height = 224
                input_width = 224
                input_mean = 0
                input_std = 255

                im = Image.fromarray(self.img)
                # im= im.convert('LA')

                im.resize((input_height, input_width), Image.ANTIALIAS)

                image_array = np.array(im)[:, :, 0:3]  # Select RGB channels only.
                # cv2.resize(img,(input_width,input_height))
                # np.array(im)[:, :, 0:3]  # Select RGB channels only.

                float_caster = tf.cast(image_array, tf.float32)
                #print(sys.getsizeof(float_caster))
                dims_expander = tf.expand_dims(float_caster, 0);
                resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
                normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
                #print(normalized)
                #sess = tf.Session()
                t = sess.run(normalized)





















                input_name = "import/" + self.input_layer
                output_name = "import/" + self.output_layer

                input_operation = self.graph.get_operation_by_name(input_name)
                #print(input_operation)
                output_operation = self.graph.get_operation_by_name(output_name)

                #print(len(t))


                results = sess.run(output_operation.outputs[0], {input_operation.outputs[0]: t})

                #print(sys.getsizeof(sess))

                results = np.squeeze(results)

                top_k = results.argsort()[-5:][::-1]
                labels = self.load_labels(self.label_file)
                # time.sleep(0.001)

                same_prediction = False
                highest_value_index = top_k[0]
                original_highest_value_index = highest_value_index
                if (highest_value_index == 1):
                    highest_value_index = 10
                elif (highest_value_index == 0):
                    highest_value_index = 1


                if (results[original_highest_value_index] > 0.7 ):


                    if ((self.current_location + 1 == highest_value_index) or (
                            self.current_location - 1 == highest_value_index)):
                        predicting_location = original_highest_value_index
                        self.current_location = highest_value_index

                    else:
                        same_prediction = True;

                else:
                    same_prediction = True
                # self.current_location=highest_value_index
                current_index = self.current_location
                if (self.current_location == 1):
                    current_index = 0
                elif (self.current_location == 10):
                    current_index = 1
                if (same_prediction):
                    predicting_location = current_index

                # print("Current ", labels[predicting_location])
                # print(labels[top_k[0]],results[top_k[0]])
                # for i in top_k:
                # print(labels[i], results[i])
                # print(" ")
                self.visualize_func(predicting_location);

            # print(" new frame")

        #  cv2.waitKey(1)

        # count += 1

        # print(datetime.datetime.time(datetime.datetime.now()))

        # file_name = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/frame1008.jpg"

    def main2(self):
        print("start main in prediction")

        self.model_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_graph.pb"
        self.label_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_labels.txt"
        # self.model_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_graph.pb"
        # self.label_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_labels.txt"
        self.first_pointer = False
        self.input_height = 224
        self.input_width = 224
        self.input_mean = 0
        self.input_std = 255
        self.input_layer = "Placeholder"
        self.output_layer = "final_result"
        self.graph = self.load_graph(self.model_file)
        #print(sys.getsizeof(self.graph))
        self.current_location = 1
        self.old_location_for_direction = 1
        self.count = 6113
        self.location = ""
        self.direction = ""
        self.queue=Queue.Queue()
        # /media/cola/EDU
        #self.video_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/1.mp4"
        #"E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/5.mp4"









        # self.cap = cv2.VideoCapture("E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/sample_video.mp4")
        #print(self.video_file)
        self.cap = cv2.VideoCapture(self.video_file)
        # "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/sample_video.mp4")
        ret, self.img = self.cap.read()

        self.img2 = self.img;
        self.location_image = self.img2

        ##UI part

        # initialize the root window and image panel

        self.window = tkinter.Tk()
        self.window.title("Tkinter and OpenCV")
        self.video_source = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/8.mp4"

        # open video source (by default this will try to open the computer webcam)
        #self.vid = MyVideoCapture(self.video_source)
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self.window, width=426, height=546)
        self.canvas.pack()
        # Button that lets the user take a snapshot
        #self.btn_snapshot = tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        #self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        #self.delay = 15
        #self.update()
        #self.window.mainloop()

        ##


        # /media/cola/EDU/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows

        # self.read_frame_thread = threading.Thread(name="read_frame", target= self.readframe_func)
        # self.read_frame_thread.setDaemon(True)
        # self.read_frame_thread.start()
        # self.prediction_thread = threading.Thread(name='prediction', target=self.output_frame_details)
        # self.prediction_thread.setDaemon(True)
        # self.prediction_thread.start()
        # self.visualize_thread = threading.Thread(name="visualize", target=self.visualize_func )
        # self.visualize_thread.setDaemon(True)
        # self.visualize_thread.start()

        # surf facts

        self.surf = cv2.xfeatures2d.SIFT_create()

        # while(True):
        self.readframe_func();

        # print(read_frame_thread.is_alive())
        # print(prediction_thread.is_alive())
        # print(visualize_thread.is_alive())
        # print("  ")
        # time.sleep(1)
        # pass


#run = prediction()
#run.main2()