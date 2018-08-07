import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage import feature


#cv2.imshow('ds',img)

import glob
image_list = []
for filename in glob.glob('*.jpg'):

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eps=1e-7
    numPoints=24
    radius=8
    lbp = feature.local_binary_pattern(img, numPoints,radius, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(),bins=np.arange(0,numPoints + 3),range=(0,numPoints + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    plt.hist(hist)
    plt.suptitle(filename, fontsize=10)

    plt.savefig('LBP/'+filename)
    plt.close() 

