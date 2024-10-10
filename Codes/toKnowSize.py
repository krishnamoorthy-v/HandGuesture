import cv2
import numpy as np
img = cv2.imread("download.png")
print("**************************")
print(img)
print("***************************")
print("one", len(img))
print("two", len(img[0]))
print("three", len(img[0][1]))
print("***********************")

#
# n = np.array([[5,4],[3,5]])
#
# print(type(n))
# print(type(img))
#
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# cv2.imshow("gray", img1)
# cv2.imshow("color", img2)
# cv2.imshow("unchanged", img3)
#
# print(img)
# print(dir(img))
# print("Height ")
# print("size of img", img.size)
# print("shape of img", img.shape)

print("**************************************")

n = np.array([[[i for i in range(0, 3)] for i in range(0, 250)] for i in range(0, 250)])

cv2.imshow("new creation", n)
print(n)

print("***************************************")
cv2.waitKey(0)
