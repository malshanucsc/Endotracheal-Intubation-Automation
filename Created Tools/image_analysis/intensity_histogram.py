import cv2
from matplotlib import pyplot as plt

from PIL import Image
import glob
image_list = []
for filename in glob.glob('*.jpg'):
    

    img = cv2.imread(filename)
    img = img[33:534,126:581]
    #cv2.imshow(filename,img)
    plt.hist(img.ravel(),256,[0,256]);
    plt.suptitle(filename, fontsize=10)

    plt.savefig('histogram_set/'+filename)
    plt.close() 
        
    #plt.show()
