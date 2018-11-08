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
#import queue
from PIL import Image
import datetime
import multiprocessing
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

    def read_tensor_from_image_file(self, img, input_height=299, input_width=299, input_mean=0, input_std=255):
        im = Image.fromarray(img)
        # im= im.convert('LA')

        im.resize((input_height, input_width), Image.ANTIALIAS)

        image_array = np.array(im)[:, :, 0:3]  # Select RGB channels only.
        # cv2.resize(img,(input_width,input_height))
        # np.array(im)[:, :, 0:3]  # Select RGB channels only.

        float_caster = tf.cast(image_array, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0);
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.Session()
        result = sess.run(normalized)


        return result

    def load_labels(self, label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label

    def output_frame_details(self,input_frame_queue,prediction_queue,visualize_queue):

        self.model_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_graph.pb"
        self.label_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_labels.txt"

        self.input_height = 224
        self.input_width = 224
        self.input_mean = 0
        self.input_std = 255
        self.input_layer = "Placeholder"
        self.output_layer = "final_result"
        self.graph = self.load_graph(self.model_file)
        self.current_location = 1



        while(True):
            #print(self.prediction_queue.qsize(), "   ", self.visualize_queue.qsize())

            if(not (input_frame_queue.empty())):
                #print("running prediction")
                #print("predict start  ",datetime.datetime.now())

                duplicate_frame=input_frame_queue.get()
                #print(duplicate_frame)
                visualize_queue.put(duplicate_frame)
                t = self.read_tensor_from_image_file(duplicate_frame,input_height=self.input_height,input_width=self.input_width,input_mean=self.input_mean,input_std=self.input_std)

                input_name = "import/" + self.input_layer
                output_name = "import/" + self.output_layer

                input_operation = self.graph.get_operation_by_name(input_name)

                output_operation = self.graph.get_operation_by_name(output_name)

                with tf.Session(graph=self.graph) as sess:
                    results = sess.run(output_operation.outputs[0],{
                        input_operation.outputs[0]: t})

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
                if (results[original_highest_value_index] > 0.85):

                    if ((self.current_location + 1 == highest_value_index) or (self.current_location - 1 == highest_value_index)):

                        prediction_queue.put(original_highest_value_index)
                        self.current_location = highest_value_index

                    else:
                        self.same_prediction = True;

                else:
                    self.same_prediction = True
                # self.current_location=highest_value_index
                current_index = self.current_location
                if (self.current_location == 1):
                    current_index = 0
                elif (self.current_location == 10):
                    current_index = 1
                if (self.same_prediction):
                    prediction_queue.put(current_index)

                #print("predict end  ",datetime.datetime.now())

            else:
                print("waiting in prediction")
                time.sleep(0.01);



    def visualize_func(self,prediction_queue,visualize_queue):
        self.location = ""
        self.count = 1

        while(True):


            if((not prediction_queue.empty())and(not visualize_queue.empty())):
                #time.sleep(0.1)

                #print("running visualize")
                #print("visualize start  ",datetime.datetime.now())


                file_name = prediction_queue.get()
                if (file_name == 0):
                    file_name = 1
                elif (file_name == 1):
                    file_name = 10
                new_location = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/locations/cropped_size/location" + str(
                    file_name) + ".jpg"
                # cb=cv2.imread(new_location)

                # cv2.imshow("image",cb)
                if (self.location != new_location):
                    self.location_image = cv2.imread(new_location)
                    self.location = new_location


                vis = np.vstack((visualize_queue.get(), self.location_image))

                write_name = "Demo/frame3_" + str(self.count) + ".jpg"
                self.count += 1
                cv2.imshow("Video", vis)
                cv2.waitKey(1)
                #cv2.imwrite(write_name, vis)
                #print("visualize end  ", datetime.datetime.now())

            else:
                print("waiting in visualize")



    def readframe_func(self,input_frame_queue):


        cap = cv2.VideoCapture(
            "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/sample_video.mp4")
        while(True):
            #time.sleep(0.1)
            #print("readframe start  ", datetime.datetime.now())
            if (cap.isOpened()):

                ret, self.img = cap.read()


                self.img2 = self.img;

                self.img = self.img[33:534, 126:581]

                input_frame_queue.put(self.img)
                #print("running input frame")

            #print("readframe end  ", datetime.datetime.now())






#        self.location_image = self.img2
if __name__ == '__main__':

    run = prediction()

    input_frame_queue = multiprocessing.Queue();
    prediction_queue = multiprocessing.Queue();
    visualize_queue = multiprocessing.Queue();

    read_frame_process = multiprocessing.Process(target=run.readframe_func, args=(input_frame_queue,))

    read_frame_process.start()

    prediction_process = multiprocessing.Process(target=run.output_frame_details, args=(
    input_frame_queue, prediction_queue, visualize_queue,))
    prediction_process.start()
    visualize_process = multiprocessing.Process(target=run.visualize_func,
                                                args=(prediction_queue, visualize_queue,))
    visualize_process.start()

###################################### cola rework


####test pycharm integration with git