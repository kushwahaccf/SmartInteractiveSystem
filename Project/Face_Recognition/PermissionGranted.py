import cv2
import numpy as np
import face_recognition
import os
from Project.gui.Functions.Speak import Speak
from Project.virtual_mouse.VirtualMouse import HandTrackingApp
import threading
import time


class SystemFaceRecognition:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.path = 'G:\\A+\\College Project\\Face_Recognition\\ImagesAttendance'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        self.encodeListKnown = []
        self.wait=5
        self.displayMessage=0
        self.video_path="..\\Resources\\videos\\face-recognition.mp4"
        # Load the video file

    def video_overlay_thread(self,video_path, frame_video, lock, video_end_reached):
        video = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video.read()

            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            with lock:
                frame_video[0] = frame.copy()

            if video_end_reached.is_set():
                break

        video.release()

    def waiting(self):
        time.sleep(5)
        self.wait=0


    def find_encodings(self):
        encodeList = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        self.encodeListKnown = encodeList

    def run_recognition_system(self):

        self.load_images()
        self.find_encodings()
        print("Encoding complete")


        while True:

            success, img = self.cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgcopy=np.copy(img)
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex] :
                    name = self.classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(imgcopy, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(imgcopy, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(imgcopy, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    if self.wait==0:
                        print('permission Granted...')
                        speak=Speak('Permission Granted')
                        speakThread=threading.Thread(target=speak.speak())
                        speakThread.start()
                        self.displayMessage=1
                        self.cap.release()
                        cv2.destroyAllWindows()
                        virtualMouse = HandTrackingApp()
                        virtualMouse.run()


        self.cap.release()
        cv2.destroyAllWindows()

