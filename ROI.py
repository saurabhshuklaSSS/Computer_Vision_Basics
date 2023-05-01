import cv2
import numpy as np

img = cv2.imread("dataset/flower.webp")


print(img.shape)

roi = img[50:200, 50:150]

img[50:200, 100:200] = roi
img[50:200, 150:250] = roi
img[50:200, 200:300] = roi
img[50:200, 100:200] = roi
# cv2.imshow("ROI", roi)
cv2.imshow("Flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()