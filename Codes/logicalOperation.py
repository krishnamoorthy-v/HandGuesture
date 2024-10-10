import cv2
img1 = cv2.imread("dog.jpeg", 0)
img2 = cv2.imread("download.jpeg", 0)

img1 = img1[:240, :250]

img2 = img2[:240, :250]
print(img1.shape, img1.size)
print(img2.shape, img2.size)

print(img1.size == img2.size)

and_ = cv2.bitwise_and(img1, img2)

cv2.imshow("hori", img1)
cv2.imshow("vertical", img2)
cv2.imshow("and", and_)
cv2.waitKey(0)

# def a(b):
#     b = b.append(5)
# c = [1, 2, 3, 4]
# a(c)
# print(len(c))