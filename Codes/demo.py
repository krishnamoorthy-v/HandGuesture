import mediapipe as mp
import cv2


cam = cv2.VideoCapture(0)
hand_detect = mp.solutions.hands.Hands()
draw_utils = mp.solutions.drawing_utils
while True:
    _, frame = cam.read()
    frame_fliped = cv2.flip(frame,1 )
    f_w, f_y, _ = frame_fliped.shape
    rgb_frame = cv2.cvtColor(frame_fliped, cv2.COLOR_BGR2RGB)
    # unkown_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2LUV)
    # lab_frame = cv2.cvtColor(frame_fliped, cv2.COLOR_BGR2LAB)
    output = hand_detect.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_utils.draw_landmarks(frame_fliped, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*f_w)
                y = int(landmark.y*f_y)
                # if id == 4:
                #     cv2.circle(i)
    cv2.imshow("rgb frame",frame_fliped)
    # cv2.imshow("lab frame",lab_frame)
    # cv2.imshow("lab frame1",unkown_frame)

    if(ord("q")==cv2.waitKey(1)):
        break


