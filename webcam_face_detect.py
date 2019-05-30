import cv2
import sys
import logging as log
import datetime as dt 
from time import sleep

casc_path = "./haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)
log.basicConfig(filename='webcam.log', level=log.INFO)

# set video source to default webcam
video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load cam.')
        sleep(5)
        pass

    # Capture frame by frame
    ret, frame = video_capture.read()

    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rect around face
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255) ,2)
    
    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display resulting frame
    cv2.imshow('Video', frame)

# When everyhing done, release the capture
video_capture.release()
cv2.destroyAllWindows()