import cv2 as cv
im = cv.imread(r'D:\Saves\Python\ImgPro\images\PXL.jpg', cv.IMREAD_COLOR)
assert im is not None

cv.namedWindow('Image', cv.WINDOW_NORMAL)
cv.imshow('Image', im)
cv.waitKey(0)
im[:, :, 0:2] = 0
cv.imshow('Image', im)
cv.waitKey(0)
cv.destroyAllWindows()