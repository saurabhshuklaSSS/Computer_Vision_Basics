import cv2
import cv2
import cv2
import numpy as np

def cross(x):
    pass


#blank image
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Color Picker Trackbars")


#creating switch
s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1, "Color Picker Trackbars", 0, 1, cross)


#creating rgb trackbars

cv2.createTrackbar("R", "Color Picker Trackbars",0, 255, cross)
cv2.createTrackbar("G", "Color Picker Trackbars",0, 255, cross)
cv2.createTrackbar("B", "Color Picker Trackbars",0, 255, cross)

while True:
    cv2.imshow("Color Picker Trackbars", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break



    #now getting trackbars position
    s = cv2.getTrackbarPos(s1, "Color Picker Trackbars")
    r = cv2.getTrackbarPos("R", "Color Picker Trackbars")
    g = cv2.getTrackbarPos("G", "Color Picker Trackbars")
    b = cv2.getTrackbarPos("B", "Color Picker Trackbars")


    if s == 0:
        img[:] = 0
    else:
        img[:] = [r, g, b]
cv2.destroyAllWindows()
