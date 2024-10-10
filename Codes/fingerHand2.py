import time

import pyautogui as gui
import numpy as np
import cv2 as cv
import mediapipe as mp
from selenium import webdriver


hand_det = mp.solutions.hands.Hands()
draw_det = mp.solutions.drawing_utils

cam = cv.VideoCapture(0)
# def fingure_detect(land_location):
#     for id, loc in enumerate(land_location):

fingerTips = [4, 8, 12, 16, 20]
finger = [0, 0, 0, 0, 0]
finger_coor = []

open_status = 0
while True:
    _, frame = cam.read()
    flipframe = cv.flip(frame, 1)
    rgbframe = cv.cvtColor(flipframe, cv.COLOR_BGR2RGB)
    hands = hand_det.process(rgbframe)
    h, w, _ = flipframe.shape
    
    if hands.multi_hand_landmarks:
        for hand in hands.multi_hand_landmarks:
            draw_det.draw_landmarks(flipframe, hand, mp.solutions.hands.HAND_CONNECTIONS)
            for id, location in enumerate(hand.landmark):
                coordinate_on_camera = [id, int(location.x * w), int(location.y * h)]
                finger_coor.append(coordinate_on_camera)
                
            for i in range(1, 5):
                if i == 1:
                    print(finger_coor[i][2] - finger_coor[i-1][1])
                if finger_coor[i][2] - finger_coor[i-1][1] < 0:
                    finger[i] = 1
                else:
                    finger[i] = 0
            if finger_coor[0][1] - finger_coor[2][0] < 0:
                finger[0] = 1
            else:
                finger[0] = 0


            total = finger.count(1)



                #print(int(hand.landmark[8].x * w) - int(hand.landmark[16].x * w))
    if finger[4] == 1:
        if open_status == 0:
            Chrome = webdriver.Chrome()

            Chrome.get(url= "file:///D:/HouseOfCorrectionPy/AIML/Lab/computer_vision/pythonProject2/AI_Virtual_Mouse_ijariie19200.pdf")
            Chrome.maximize_window()
            open_status = 1

    elif finger[4] == 0:
        if open_status == 1:
            Chrome.close()
            open_status = 0

    if open_status == 1:
        if (finger[3] == 1 and finger[2] == 1) and finger.count(1) == 4:

            # print("hi", int(hand.landmark[8].x * w) - int(hand.landmark[12].x * w))
            if int(hand.landmark[8].x *w)- int(hand.landmark[12].x * w) >= -35:
                if hand.landmark[8].y < hand.landmark[12].y:
                #print("hi", int(hand.landmark[8].x *w)- int(hand.landmark[12].x * w))
                    gui.scroll(-200)
                else:
                    gui.scroll(200)


    cv.putText(flipframe, f"finger: {finger.count(1)}", org=(20, 40), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=5, color = (0, 0, 255))
    cv.imshow("fingure", flipframe)
    if cv.waitKey(1) == ord("q"):
        break
