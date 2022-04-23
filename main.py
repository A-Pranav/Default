import cv2
import time
import datetime
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont


def move_detect(mxperson):
    maxFacesAllowed=mxperson

    print(maxFacesAllowed)
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    right_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")

    left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")

    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


    detection = False
    detection_stopped_time = None
    timer_started = False
    SECONDS_TO_RECORD_AFTER_DETECTION = 5
    frame_size = (640,480)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.31,4)

        eyes = eye_cascade.detectMultiScale(gray, 1.35, 4)

        leye = left_eye_cascade.detectMultiScale(gray, 1.28, 4)

        reye = right_eye_cascade.detectMultiScale(gray, 1.29, 3)


        bodies = body_cascade.detectMultiScale(gray, 1.2, 5)

        if (len(faces) or len(bodies) or len(eyes) or len(leye) or len(reye) > 0):
            if detection:
                timer_started = False
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20.0, frame_size)
                print("Started Recording!")
        elif detection:
            if timer_started:
                if (time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION):
                    detection = False
                    timer_started = False
                    out.release()
                    print("Stop Recording!")
            else:
                timer_started = True
                detection_stopped_time = time.time()

        if detection:
            out.write(frame)

        for (x, y, width, height) in faces:
            if len(faces) + len(bodies)> 0:
                print(len(faces),"persons detected")
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (25, 50, 255), 2)


        for (x, y, width, height) in eyes:
            if len(eyes)> 0:
                print(len(eyes)," eyes detected")
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 15), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (25, 50, 255), 2)
        
        
        for (x, y, width, height) in leye:
            if len(leye)> 0:
                print(len(eyes)," left eye detected")
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (25, 50, 255), 2)


        for (x, y, width, height) in leye:
            if len(leye)> 0:
                print(len(eyes)," right eye detected")
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (25, 50, 255), 2)
        
        
        cv2.imshow("Camera", frame)
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        if cv2.waitKey(1) == ord("q"):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()


class App:
    def __init__(self, root):
        # setting title
        root.title("SecureWay")
        # setting window size
        width = 550
        height = 450
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=True, height=True)


        start_cam = tk.Button(root)
        start_cam["bg"] = "#F6D860"
        ft = tkFont.Font(family="Times", size=10)
        start_cam["font"] = ft
        start_cam["fg"] = "#EA5C2B"
        start_cam["justify"] = "center"
        start_cam["text"] = "Start Camera"
        start_cam.place(x=50, y=90, width=200, height=75)
        start_cam["command"] = self.start_cam_command

        stop_cam_label = tk.Label(root)
        stop_cam_label["bg"] = "#FF7F3F"
        ft = tkFont.Font(family="Times", size=10)
        stop_cam_label["font"] = ft
        stop_cam_label["fg"] = "#000000"
        stop_cam_label["justify"] = "center"
        stop_cam_label["text"] = "Press q to stop camera"
        stop_cam_label.place(x=300, y=90, width=200, height=75)

    def start_cam_command(numb):
            print ("numb==",numb)
            move_detect(numb)
    


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
