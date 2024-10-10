import cv2
import mediapipe as mp
import pyautogui as gui
import shelve
import numpy as np

cam = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

x_axis = np.array([i for i in range(0, gui.size().width)])
y_axis = np.array([i for i in range(0, gui.size().height)])
obtained_x_axis = np.array([])
obtained_y_axis = np.array([])

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands = hand.process(rgbframe)
    w, h, _ = frame.shape
    if hands.multi_hand_landmarks:
        for hand_landmark in hands.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmark, mp.solutions.hands.HAND_CONNECTIONS)
            for id, landmark in enumerate(hand_landmark.landmark):
                np.append(obtained_x_axis, landmark.x)
                np.append(obtained_y_axis, landmark.y)
                with shelve.open("coverageTest") as f:
                    f["x_axis"] = obtained_x_axis
                    f["y_axis"] = obtained_y_axis

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break