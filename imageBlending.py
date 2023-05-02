import cv2

img1 = cv2.imread("dataset/flower.webp")
img1 = cv2.resize(img1, (400, 600))
img2 = cv2.imread("dataset/image2.jpeg")
img2 = cv2.resize(img2, (400, 600))

cv2.imshow("Flower1", img1)
cv2.imshow("Flower2", img2)

img3 = cv2.add(img1, img2)
cv2.imshow("MergedImage", img3)

img4 = cv2.addWeighted(img1, 0.9, img2, 0.1, 1)
cv2.imshow("MergedImg2", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()