import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, misc

from skimage import feature, measure
from skimage.filter import canny

#Feature detection without using OpenCV

def scipy_examples():
	img = misc.imread('1.jpg')
	im = ndimage.gaussian_filter(img, 5)
	sx = ndimage.sobel(im, axis=0, mode='constant')
	sy = ndimage.sobel(im, axis=1, mode='constant')
	pot = np.hypot(sx,sy)
	plt.show()
	plt.imshow(pot)

def skimage_example():
	img = misc.imread('1.jpg')
	im = ndimage.gaussian_filter(img, 4)
	print(img)
	result = canny(img)
	contours = measure.find_contours(gimg, 0.8)
	print(contours, ...)
