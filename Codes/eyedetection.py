import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# cap = cv2.VideoCapture(0)
# while True:
#     _, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,0), 5)
#     cv2.imshow("img", img)

img = cv2.imread("faces2.jpeg", 0)
faces = face_cascade.detectMultiScale(img, 1.1, 6)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
    cv2.imshow("face",img)

cv2.waitKey(0)