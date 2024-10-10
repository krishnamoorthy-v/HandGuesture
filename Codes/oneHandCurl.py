import mediapipe as mp
from toolMade.mediapipemath import equalideandistance
import cv2

pose = mp.solutions.pose.Pose()
draw = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)
count = 0
status = 0
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = pose.process(rgbframe)
    h, w, _ = frame.shape

    if output.pose_landmarks:
        draw.draw_landmarks(frame, output.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        pose_landmark = output.pose_landmarks
        for id, landmarks in enumerate(pose_landmark.landmark):
            x = int(landmarks.x*w)
            y = int(landmarks.y*h)

            if id in [11, 15]:
                cv2.circle(frame, center=(x, y), color=(255, 0, 0), radius=5, thickness=5)
                if id == 11:
                    if equalideandistance(landmarks, pose_landmark.landmark[15], w, h) < 80:
                        if status == 0:
                            count += 1
                            status = 1
                    if equalideandistance(landmarks, pose_landmark.landmark[15], w, h) > 400:
                        status = 0
                    #print(equalideandistance(landmarks, pose_landmark.landmark[15], w, h))
                cv2.putText(frame, text=f"count: {str(count)}", org=(20, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(0, 0, 255), fontScale=2, thickness=4)

    cv2.imshow("Pose", frame)
    if cv2.waitKey(1) == ord("q"):
        break