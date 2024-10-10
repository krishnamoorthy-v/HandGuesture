# import cv2
# import numpy as np
#
# # Read the image
# image = cv2.imread('images.jpeg')
#
# # Convert the image from BGR to HSV
# #rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# # Define the color range for detection (in HSV)
# lower_color_blue = np.array([156, 188, 230])
# upper_color_blue = np.array([4, 34, 109])
#
# lower_color_green = np.array([25, 52, 72])
# upper_color_green = np.array([102, 255, 255])
#
# upper_color_red = np.array([176, 255, 255])
# lower_color_red = np.array([161, 255, 255])
# # Create a mask using the specified color range
# color_mask_green = cv2.inRange(image, lower_color_green, upper_color_green)
# color_mask_red = cv2.inRange(image, lower_color_red, upper_color_red)
# color_mask_blue = cv2.inRange(image, lower_color_blue, upper_color_blue)
# # Apply the mask to the original image
# result_green = cv2.bitwise_and(image, image, mask=color_mask_green)
# result_red = cv2.bitwise_and(image, image, mask=color_mask_red)
# result_blue = cv2.bitwise_and(image, image, mask=color_mask_blue )
#
# # Display the original image, mask, and result
# cv2.imshow('Original Image', image)
#
# cv2.imshow('green', result_green)
# cv2.imshow('red', result_red)
# cv2.imshow('blue', result_blue)
#
# cv2.waitKey(0)
#




import cv2
import numpy as np

img = cv2.imread("images.jpeg")

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])

lower_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])

lower_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

blue = cv2.inRange(hsv_image, lower_blue, high_blue)
green = cv2.inRange(hsv_image, lower_green, high_green)
red = cv2.inRange(hsv_image, lower_red, high_red)

blue_color = cv2.bitwise_and(img, img, mask=blue)
green_color = cv2.bitwise_and(img, img, mask=green)
red_color = cv2.bitwise_and(img, img, mask=red)

cv2.imshow("orginal", img)
cv2.imshow("Blue", blue_color)
cv2.imshow("Red", red_color)
cv2.imshow("Green", green_color)


cv2.imshow("HSV", hsv_image)
cv2.waitKey(0)