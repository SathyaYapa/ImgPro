import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread(r"D:\Saves\Python\ImgPro\images\PXL.jpg", cv.IMREAD_GRAYSCALE)
assert im is not None

h = np.zeros(256)
h = [np.sum(im == i) for i in range(256)]


plt.bar(range(256), h)

plt.show()