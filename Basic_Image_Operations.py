import cv2

import numpy as np

img = cv2.imread("dataset/flower.webp")
# img = cv2.resize(img, (300, 200))

#printing size of the image
print(img.shape)
print(img.size)

print(cv2.split(img))

r, g, b = cv2.split(img)

# cv2.imshow("Red", r)
# cv2.imshow("Green", g)
# cv2. imshow("Blue", b)
# cv2.imshow("OGImage", img)

# mergeImage = cv2.merge((r, g, g))
# cv2.imshow("MergeImage", mergeImage)

blue, green, red = colors = img[300, 280]

print(colors)

# cv2.waitKey(0)
# cv2.destroyAllWindows()