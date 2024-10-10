from django.http import HttpResponse
import threading
import requests
import pyautogui as gui
import cv2 as cv
import mediapipe as mp

finger_count = 0
prev_finger = 0

def fingerEngine():

    hand_det = mp.solutions.hands.Hands()
    draw_det = mp.solutions.drawing_utils

    cam = cv.VideoCapture(0)
    # def fingure_detect(land_location):
    #     for id, loc in enumerate(land_location):

    finger = [0, 0, 0, 0, 0]
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
                    coordinate_on_camera = (int(location.x * w), int(location.y * h))

                    if id == 4:
                        cv.circle(flipframe, coordinate_on_camera, 10, (255, 0, 255), 10)
                        if coordinate_on_camera[0] - int(hand.landmark[2].x * w) < 0:
                            finger[4] = 1
                        else:
                            finger[4] = 0

                    elif id == 8:
                        cv.circle(flipframe, coordinate_on_camera, 10, (255, 0, 255), 10)
                        if coordinate_on_camera[1] - int(hand.landmark[7].y * h) < 0:
                            finger[3] = 1
                        else:
                            finger[3] = 0

                    elif id == 12:
                        cv.circle(flipframe, coordinate_on_camera, 10, (255, 0, 255), 10)
                        if coordinate_on_camera[1] - int(hand.landmark[11].y * h) < 0:
                            finger[2] = 1
                        else:
                            finger[2] = 0

                    elif id == 16:
                        cv.circle(flipframe, coordinate_on_camera, 10, (255, 0, 255), 10)
                        if coordinate_on_camera[1] - int(hand.landmark[15].y * h) < 0:
                            finger[1] = 1
                        else:
                            finger[1] = 0

                    elif id == 20:
                        cv.circle(flipframe, coordinate_on_camera, 10, (255, 0, 255), 10)
                        if coordinate_on_camera[1] - int(hand.landmark[19].y * h) < 0:
                            finger[0] = 1
                        else:
                            finger[0] = 0

                    # print(int(hand.landmark[8].x * w) - int(hand.landmark[16].x * w))
        # if finger[4] == 1:
        #     if open_status == 0:
        #         Chrome = webdriver.Chrome()
        #
        #         Chrome.get(
        #             url="file:///D:/HouseOfCorrectionPy/AIML/Lab/computer_vision/pythonProject2/AI_Virtual_Mouse_ijariie19200.pdf")
        #         Chrome.maximize_window()
        #         open_status = 1
        #
        # elif finger[4] == 0:
        #     if open_status == 1:
        #         Chrome.close()
        #         open_status = 0

        if open_status == 1:

            if (finger[3] == 1 and finger[2] == 1) and finger.count(1) == 4:
                print("hi", int(hand.landmark[8].x * w) - int(hand.landmark[12].x * w))
                if int(hand.landmark[8].x * w) - int(hand.landmark[12].x * w) >= -35:
                    if hand.landmark[8].y < hand.landmark[12].y:
                        # print("hi", int(hand.landmark[8].x *w)- int(hand.landmark[12].x * w))
                        gui.scroll(-200)
                    else:
                        gui.scroll(200)
        # finger_count = int(finger_count(1))
        global finger_count, prev_finger
        finger_count = finger.count(1)

        cv.putText(flipframe, f"finger: {finger.count(1)}", org=(20, 40), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1,
                   thickness=5, color=(0, 0, 255))
        cv.imshow("fingure", flipframe)
        if (finger_count != prev_finger):
            t2 = threading.Thread(target=lambda: requests.get(url="http://127.0.0.1:8000/get-data/"))
            t2.start()
            prev_finger = finger_count
            print(finger_count)

        if cv.waitKey(1) == ord("q"):
            break

t1 = threading.Thread(target=fingerEngine)
t1.start()


def get_data(request):
    data = finger_count

    # api = "3UEU78ZD0K4MBQGM"
    # try:
    #     requests.get(url="https://api.thingspeak.com/update?api_key={}&field1={}".format(api, data))
    #     print("Data sended successfully")
    # except:
    #     print("Error while sending data")
    return HttpResponse(data)
