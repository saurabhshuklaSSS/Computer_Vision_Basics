import cv2
import numpy as np

img = cv2.imread("dataset/flower.webp")

while True:
    HSVImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    u_v = np.array([219, 71, 252])
    l_v = np.array([203, 5, 247])

    mask = cv2.inRange(HSVImg, u_v, l_v)

    cv2.imshow("mask", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()