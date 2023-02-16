import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread(r"D:\Saves\Python\ImgPro\images\BrainProtonDensitySliceBorder.png", cv.IMREAD_GRAYSCALE)
assert im is not None


t = np.arange(0,256).astype(np.uint8)
t[0:99]=0
t[201:255]=0
plt.plot(t)
print(t.shape)

g = t[im]




cv.namedWindow('image', cv.WINDOW_KEEPRATIO)

cv.imshow('image', im)
cv.waitKey(0)
cv.imshow('image', g)
cv.waitKey(0)

cv.destroyAllWindows()

