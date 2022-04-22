import cv2
import time
import datetime
import urllib.request
import numpy
import os

maxFacesAllowed = 1

# WURL="rtsp://hello:1234@192.168.43.205:6969/h264Preview_01_main"
# os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

# cap = cv2.VideoCapture(WURL, cv2.CAP_FFMPEG)

# imgResp=urllib.request.urlopen(WURL)
# imgNP=numpy.array(bytearray(imgResp.read()),dtype=numpy.uint8)
# img=cv2.imdecode(imgNP,-1)
# cap = cv2.VideoCapture(img)
# cap = cv2.VideoCapture("rtsp://hello:1234@192.168.43.205:6969/h264Preview_01_main")
# cap = cv2.VideoCapture("rtsp://hello:1234@192.168.43.205:6969/h264Preview_01_main")


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
face_cascade2 = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
)
face_cascade3 = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml"
)
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5
frame_size = (int(cap.get(100)), int(cap.get(60)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
while True:
    _, frame = cap.read()
    print(_)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    faces2 = face_cascade2.detectMultiScale(gray, 1.25, 4)
    faces3 = face_cascade3.detectMultiScale(gray, 1.2, 4)
    bodies = body_cascade.detectMultiScale(gray, 1.2, 5)
    
    if len(faces) + len(bodies) or len(faces2) + len(bodies) or len(faces3) + len(bodies)> maxFacesAllowed:
    # if len(faces2) + len(bodies) > 0:
        # if len(bodies) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if (
                time.time() - detection_stopped_time
                >= SECONDS_TO_RECORD_AFTER_DETECTION
            ):
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    # for (x, y, width, height) in faces:
    for (x, y, width, height) in faces2:
        if len(faces) > maxFacesAllowed:
        # if len(faces2) > maxFacesAllowed:
            # cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
            cv2.rectangle(frame, (10, 10), (50, 50), (255, 50, 0), 2)
            print("2nd person detected")
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 255), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 255), 2)

    # for (x, y, width, height) in bodies:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)
    # for (x, y, width, height) in faces:
    #     # if len(faces) + len(bodies)>maxFacesAllowed:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    # for (x, y, width, height) in bodies:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
