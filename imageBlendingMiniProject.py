import cv2
import numpy as np

def blend(x):
    pass

img1 = cv2.imread("dataset/flower.webp")
img1 = cv2.resize(img1, (400, 600))
img2 = cv2.imread("dataset/image2.jpeg")
img2 = cv2.resize(img2, (400, 600))


img = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow("win")

#creating switch
s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1, "win", 0, 1, blend)
cv2.createTrackbar("Value", "win",0, 100, blend)


while True:
    s = cv2.getTrackbarPos(s1, "win")
    V = cv2.getTrackbarPos("Value", "win")
    n = float(V/100)
    # print(n)

    if s == 0:
        newImg = img[:]
    else:
        newImg = cv2.addWeighted(img1, n, img2, 1-n, 1)
    cv2.imshow("Result", newImg)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows