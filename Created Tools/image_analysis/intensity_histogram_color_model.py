import cv2
from matplotlib import pyplot as plt

from PIL import Image
import glob
image_list = []
for filename in glob.glob('*.jpg'):
    

    img = cv2.imread(filename)
    img = img[33:534,126:581]
    cv2.imshow("ss",img)
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
        plt.suptitle(filename, fontsize=10)
        
    plt.show()
