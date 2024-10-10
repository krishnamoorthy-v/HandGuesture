import cv2 as cv
import mediapipe as mp
from toolMade.fingerstatus import likes, dislike

hand = mp.solutions.hands.Hands()


draw = mp.solutions.drawing_utils


cam = cv.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    obj_hands = hand.process(rgb_frame)

    if obj_hands.multi_hand_landmarks:
        for hands in obj_hands.multi_hand_landmarks:
           
            draw.draw_landmarks(frame, hands, mp.solutions.hands.HAND_CONNECTIONS)
            for id, location in enumerate(hands.landmark):
                if likes(hands.landmark):
                    cv.putText(frame, text="Like", org=(10, 20), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=5, color = (0, 0, 255))
                elif dislike(hands.landmark):
                    cv.putText(frame, text="Dislike", org=(10, 20), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=5, color = (0, 0, 255))
    cv.imshow("Video", frame)
    if cv.waitKey(1) == ord('q'):
        break