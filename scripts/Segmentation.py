
import cv2 
from matplotlib import pyplot as plt
import numpy as np
import time


def segmentImages(pathOfImage, k):
    image = cv2.imread(pathOfImage)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    new_image = image.reshape((-1,3))
    new_image = np.float32(new_image)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    _ , labels, center = cv2.kmeans(new_image, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)

    segmented_data = center[labels.flatten()]

    segmented_image = segmented_data.reshape(image.shape)
    
    plt.imsave('static/segmented.jpg',segmented_image)
    


