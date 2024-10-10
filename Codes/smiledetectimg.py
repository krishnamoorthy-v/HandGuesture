import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

img = cv2.imread("smile.jpg", 0)
img2 = cv2.resize(img, (500, 500))
faces = face_cascade.detectMultiScale(img2, 1.1, 5)
smile = smile_cascade.detectMultiScale(img2, 1.25, 20)

for (x, y, w, h) in faces:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 0), 5)
    for(x2, y2, w2, h2) in smile:
        if (x<x2 and y<y2) and (w>w2 and h>h2):
            cv2.rectangle(img2, (x2, y2), (x2+w2, y2+h2), (0,0,0), 5)
# while True:
#     _, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     smile = smile_cascade.detectMultiScale(gray, 1.25, 20)
#     for (x, y, w, h) in faces:
#         for(x2, y2, w2, h2) in smile:
#
#             if (x<x2 and y<y2) and (w>w2 and h>h2):
#                 cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (0,0,0), 5)
#     cv2.imshow("img", img)



cv2.imshow("img", img2)
cv2.waitKey(0)
