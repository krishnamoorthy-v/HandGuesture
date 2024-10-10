import cv2
import shelve

# img = cv2.imread("cat.jpeg", 0)
#
# one_dim = img.flatten()
# total = one_dim.sum()
# with shelve.open("pixel") as f:
#     f["cat"] = total
#
# cv2.imshow("cat",img)


img = cv2.imread("ver.png", 0)

one_dim = img.flatten()
total = one_dim.sum()
print(total)
with shelve.open("pixel") as f:
    expected_dog = f["dog"]
    expected_cat = f["cat"]

if(total == expected_dog):
    print("This our expected dog")
elif(total == expected_cat):
    print("This our expected cat")
else:
    print("It's not our expectation")

cv2.imshow("img", img)

cv2.waitKey(0)