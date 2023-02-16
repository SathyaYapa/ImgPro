import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = cv.imread(r"D:\Saves\Python\ImgPro\images\PXL.jpg", cv.IMREAD_GRAYSCALE)
assert im is not None

gamma=0.5
t= np.array([(i/255.)**gamma**255 for i in range (256)], dtype=np.uint8)

g = t[im]

plt.plot(t)
plt.show()


cv.namedWindow('image', cv.WINDOW_KEEPRATIO)


cv.imshow('image', im)
cv.waitKey(0)
cv.imshow('image', g)
cv.waitKey(0)

cv.destroyAllWindows()


