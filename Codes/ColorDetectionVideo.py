import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    # lower_red = np.array([161, 155, 84])
    # high_red = np.array([176, 255, 255])
    lower_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    lower_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])

    blue = cv2.inRange(hsv_image, lower_blue, high_blue)
    green = cv2.inRange(hsv_image, lower_green, high_green)
    red = cv2.inRange(hsv_image, lower_red, high_red)

    blue_color = cv2.bitwise_and(frame, frame, mask=blue)
    green_color = cv2.bitwise_and(frame, frame, mask=green)
    red_color = cv2.bitwise_and(frame, frame, mask=red)

    cv2.imshow("orginal", frame)
    cv2.imshow("Blue", blue_color)
    cv2.imshow("Red", red_color)
    cv2.imshow("Green", green_color)
    cv2.imshow("HSV", hsv_image)


    if cv2.waitKey(1) == ord("q"):
        break