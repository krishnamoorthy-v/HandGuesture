import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")


cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    smile = smile_cascade.detectMultiScale(gray, 1.5, 50)
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 5)
        for(x2, y2, w2, h2) in smile:

            if (x<x2 and y<y2) and (w>w2 and h>h2):
                cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), (0,0,0), 5)
    cv2.imshow("img", img)



    if cv2.waitKey(10) == ord("q"):
        break
