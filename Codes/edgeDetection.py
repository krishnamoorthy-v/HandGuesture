# import cv2
# cp = cv2.VideoCapture(0)
# while True:
#     _, frame = cp.read()
#     grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     can = cv2.Canny(grey_frame, 50, 100)
#     cv2.imshow("video", can)
#     cv2.waitKey(0)
#
#

import cv2
import numpy as np
cam = cv2.VideoCapture(0)
# Read an image from file

while True:
    _, frame = cam.read()
# Apply Gaussian blur with a 5x5 kernel and standard deviation of 0 (auto-calculated from kernel size)
    blurred_image = cv2.GaussianBlur(frame, (7, 7), 100)
    edge = cv2.Canny(blurred_image, 0, 100)

# Display the original and blurred images
    cv2.imshow('Original Image', frame)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow("edge detection canny", edge)

    if cv2.waitKey(1) == ord('q'):
        break

