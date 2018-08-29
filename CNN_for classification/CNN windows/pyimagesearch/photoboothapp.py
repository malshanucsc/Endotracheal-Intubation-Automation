# import the necessary packages
from __future__ import print_function

from PIL import ImageTk
import tkinter as tki
import threading
import datetime
import imutils
import os
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
#from CustomQueue import CustomQueue




class PhotoBoothApp:
	def __init__(self, vs, outputPath):
		# store the video stream object and output path, then initialize
		# the most recently read frame, thread for reading frames, and
		# the thread stop event
		self.vs = vs
		self.outputPath = outputPath
		self.frame = None
		self.thread = None
		self.stopEvent = None


		model_file = \
			"E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_graph.pb"

		self.label_file = "E:/Degree/4th year 1st semester/Project/Endotracheal-Intubation-Automation/CNN_for classification/CNN windows/tmp/output_labels.txt"
		self.input_height = 299
		self.input_width = 299
		self.input_mean = 0
		self.input_std = 255
		self.input_layer = "Placeholder"
		self.output_layer = "final_result"
		self.graph = self.load_graph(model_file)
		self.queue=CustomQueue();

		# initialize the root window and image panel
		self.root = tki.Tk()
		self.panel = None

		# create a button, that when pressed, will take the current
		# frame and save it to file
		#btn = tki.Button(self.root, text="Snapshot!",command=self.takeSnapshot)
		self.lbl = tki.Label(self.root, text="",fg = "light green",bg = "grey",font = "Verdana 10 bold")
		self.lbl.pack(side="bottom", fill="both", expand="yes", padx=10,pady=10)

		#btn.pack(side="bottom", fill="both", expand="yes", padx=10,pady=10)

		# start a thread that constantly pools the video sensor for
		# the most recently read frame
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.videoLoop, args=())
		self.thread.start()

		# set a callback to handle when the window is closed
		self.root.wm_title("PyImageSearch PhotoBooth")
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)


	def videoLoop(self):
		# DISCLAIMER:
		# I'm not a GUI developer, nor do I even pretend to be. This
		# try/except statement is a pretty ugly hack to get around
		# a RunTime error that Tkinter throws due to threading
		try:
			# keep looping over frames until we are instructed to stop
			while not self.stopEvent.is_set():
				# grab the frame from the video stream and resize it to
				# have a maximum width of 300 pixels
				self.frame = self.vs.read()
				self.frame=self.frame[33:534, 126:581]

				#cv2.imshow("haha",self.frame)
				#self.bound = Bounds(l, t, l + w, t + h)
				#imutils.crop(self.frame, *self._bound)
				#print("done")
				self.frame = imutils.resize(self.frame, width=400)
				self.output_frame_details()
				if(self.queue.isEmpty()!=True):
					self.lbl.configure(text=self.queue.getMax())
				#print(self.queue.getMax())

		
				# OpenCV represents images in BGR order; however PIL
				# represents images in RGB order, so we need to swap
				# the channels, then convert to PIL and ImageTk format
				image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image)
				image = ImageTk.PhotoImage(image)
		
				# if the panel is not None, we need to initialize it
				if self.panel is None:
					self.panel = tki.Label(image=image)
					self.panel.image = image
					self.panel.pack(side="left", padx=10, pady=10)
		
				# otherwise, simply update the panel
				else:
					self.panel.configure(image=image)
					self.panel.image = image

		except RuntimeError:
			print("[INFO] caught a RuntimeError")

	def takeSnapshot(self):
		# grab the current timestamp and use it to construct the
		# output path
		ts = datetime.datetime.now()
		filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
		p = os.path.sep.join((self.outputPath, filename))

		# save the file
		cv2.imwrite(p, self.frame.copy())
		print("[INFO] saved {}".format(filename))

	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()

	def load_graph(self,model_file):
		self.graph = tf.Graph()
		graph_def = tf.GraphDef()

		with open(model_file, "rb") as f:
			graph_def.ParseFromString(f.read())
		with self.graph.as_default():
			tf.import_graph_def(graph_def)

		return self.graph

	def read_tensor_from_image_file(self,img, input_height, input_width, input_mean, input_std):
		im = Image.fromarray(img)

		im.resize((input_height, input_width), Image.ANTIALIAS)
		image_array = np.array(im)[:, :, 0:3]  # Select RGB channels only.
		float_caster = tf.cast(image_array, tf.float32)
		dims_expander = tf.expand_dims(float_caster, 0);
		resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
		normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
		sess = tf.Session()
		result = sess.run(normalized)
		#print(resized)

		return result

	def load_labels(self,label_file):
		label = []
		proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
		for l in proto_as_ascii_lines:
			label.append(l.rstrip())
		return label

	def output_frame_details(self):
		# print(input_height)
		t = self.read_tensor_from_image_file(self.frame,input_height=self.input_height,input_width=self.input_width,input_mean=self.input_mean,input_std=self.input_std)

		input_name = "import/" + self.input_layer
		output_name = "import/" + self.output_layer

		input_operation = self.graph.get_operation_by_name(input_name)
		# print(input_operation)
		output_operation = self.graph.get_operation_by_name(output_name)

		with tf.Session(graph=self.graph) as sess:
			results = sess.run(output_operation.outputs[0], {
				input_operation.outputs[0]: t
			})

		results = np.squeeze(results)

		top_k = results.argsort()[-5:][::-1]
		labels = self.load_labels(self.label_file)
		print(labels[top_k[0]]+"  :  ",results[top_k[0]])
		if(results[top_k[0]]>0.9):
			self.queue.enqueue(labels[top_k[0]])
		#for i in top_k:
			#print(labels[i], results[i])

		#print(" ")


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if (len(self.items) >= 5):
            self.items.pop(0)
            self.items.append(item)
        else:
            self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop(0)
    def getMax(self):

        return max(self.items,key=self.items.count)