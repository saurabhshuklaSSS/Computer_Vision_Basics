import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (150, 100), (200, 250), (255, 255, 255), -1)

img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (10, 10), (170, 190), (255, 255, 255), -1)

# cv2.imshow("Image 1", img1)
# cv2.imshow("Image 2", img2)

bitor = cv2.bitwise_or(img1, img2)
# cv2.imshow("Bit Or", bitor)

bitAnd = cv2.bitwise_and(img1, img2)
# cv2.imshow("Bit And", bitAnd)

bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

bitXor = cv2.bitwise_xor(img1, img2)
cv2.imshow("Bit Xor", bitXor)

cv2.imshow("Bit Not 1", bitNot1)
cv2.imshow("Bit Not 2", bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()