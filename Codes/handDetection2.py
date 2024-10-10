import time
import cv2
import mediapipe as mp
import pyautogui
from toolMade.mouseMoves import Moves


moves = Moves()
cam = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
w_h = pyautogui.size()

velocity = 1.9
# prev_fps = 0
# new_fps = 0

mouse_down_status = 0

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands = hand.process(rgbframe)
    h, w, _ = frame.shape

 #   new_fps = time.time()
 #   fps = str(int(1 / (new_fps - prev_fps)))
 #   prev_fps = new_fps
 #   cv2.putText(img=frame, org=(20, 30), text=fps, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
 #               thickness=5, color=(0, 0, 255))

    if hands.multi_hand_landmarks:
        for hand_landmarks in hands.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            for id, lms in enumerate(hand_landmarks.landmark):
                x, y = int(lms.x * w_h.width), int(lms.y * w_h.height)
                draw_x, draw_y = int(lms.x * w), int(lms.y * h)
                cursor_y = (int(hand_landmarks.landmark[0].y * h) + int(hand_landmarks.landmark[9].y * h)) // 2

                if id == 9:
                    cv2.circle(frame, (draw_x, cursor_y), 10, (255, 0, 255), thickness=10)
                    moves.moveto(x, y)
                moves.mouse_Drag_and_Drop(hand_landmarks)

    cv2.imshow("hand", frame)
    if cv2.waitKey(1) == ord("q"):
        break
