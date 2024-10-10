import cv2
import mediapipe as mp
from toolMade.mediapipemath import equalideandistance

cam = cv2.VideoCapture(0)
face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
draw = mp.solutions.drawing_utils

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face.process(rgbframe)
    h, w, _ = frame.shape

    obj_hand = faces.multi_face_landmarks
    if obj_hand:
        for face_landmarks in obj_hand:
            draw.draw_landmarks(frame, face_landmarks, mp.solutions.face_mesh.FACEMESH_FACE_OVAL)

            for id, lms in enumerate(face_landmarks.landmark):
                draw_x, draw_y = int(lms.x * w), int(lms.y * h)

                if id in [133, 33, 160, 158, 144, 153]:
                    cv2.circle(frame, (draw_x, draw_y), 1, (255, 0, 255), thickness=1)

                if id == 160:
                    v1 = equalideandistance(face_landmarks.landmark[160], face_landmarks.landmark[144], w, h)
                    v2 = equalideandistance(face_landmarks.landmark[158], face_landmarks.landmark[153], w, h)
                    h = equalideandistance(face_landmarks.landmark[13], face_landmarks.landmark[33], w, h)
                    if (v1+v2)/h < 0.16:
                        cv2.putText(img=frame, org=(20, 30), text="closed", fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    thickness=5, color=(0, 0, 255))
                    else:
                        cv2.putText(img=frame, org=(20, 30), text="open", fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    thickness=5, color=(0, 0, 255))

    cv2.imshow("hand", frame)
    if cv2.waitKey(1) == ord("q"):
        break