import cv2

img1 = cv2.imread("dataset/flower.webp")

borderImg = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = [255,255,255])
cv2.imshow("Image", borderImg)
cv2.waitKey(0)
cv2.destroyAllWindows()