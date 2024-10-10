import cv2
import numpy
import numpy as np

n = np.array([[[0 for i in range(0, 3)] for i in range(0, 240)] for i in range(0, 240)])

for i in range(0, 240):
    for j in range(0, 240):
        for k in range(0, 3):
            if 80 <= i <= 160:
                n[i][j][k] = 250

cv2.imwrite("horizontal.png", n)
