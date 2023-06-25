import cv2
import mouse
import threading
import time
from cvzone.HandTrackingModule import HandDetector
from pyautogui import press,scroll
from playsound import playsound


class HandTrackingApp:
    def __init__(self):
        self.detector = HandDetector(detectionCon=0.9, maxHands=2)
        self.cap = cv2.VideoCapture(0)
        self.pTime = 0
        self.cam_w = 640
        self.cam_h = 480
        self.cap.set(3, self.cam_w)
        self.cap.set(4, self.cam_h)
        self.frameR = 150
        self.l_delay = 0
        self.r_delay = 0
        self.d_delay = 0
        self.p_delay = 0
        self.sound_delay = 0
        self.l_clk_thread = threading.Thread(target=self.l_clk_delay)
        self.r_clk_thread = threading.Thread(target=self.r_clk_delay)
        self.d_clk_thread = threading.Thread(target=self.d_clk_delay)
        self.p_clk_thread = threading.Thread(target=self.p_clk_delay)
        self.sound_thread = threading.Thread(target=self.play_sound)

    def run(self):
        while True:
            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            hands, img = self.detector.findHands(img, flipType=False)
            cv2.rectangle(img, (self.frameR, self.frameR), (self.cam_w - self.frameR, self.cam_h - self.frameR),
                          (0, 191, 255), 2)

            if hands:
                lmList = hands[0]['lmList']
                hand1 = hands[0]
                handtype1 = hand1["type"]
                if len(hands)==2:
                    print("Two Hands")
                ind_x, ind_y = lmList[8][0], lmList[8][1]
                mid_x, mid_y = lmList[12][0], lmList[12][1]
                thumb_x, thumb_y = lmList[4][0], lmList[4][1]

                cv2.circle(img, (ind_x, ind_y), 5, (0, 255, 255), 2)

                fingers = self.detector.fingersUp(hands[0])


                if fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and fingers[0] == 0 and handtype1 == "Right":
                    if self.l_delay == 0:
                        self.l_delay = 1
                        self.l_clk_thread.start()
                        scroll(1)

                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1 and handtype1 == "Right" \
                        and self.sound_delay == 0:
                    if abs(ind_x - mid_x) < 25:

                        if fingers[4] == 0 and self.l_delay == 0:
                            mouse.click(button="left")
                            # self.sound_thread.start()
                            self.l_delay = 1
                            # self.sound_delay = 1
                            self.l_clk_thread.start()

                        if fingers[4] == 1 and self.r_delay == 0:
                            mouse.click(button="right")
                            # self.sound_thread.start()
                            self.r_delay = 1
                            # self.sound_delay = 1
                            self.r_clk_thread.start()

                        if fingers[4] == 0 and self.d_delay == 0 and fingers[3] == 1:
                            mouse.double_click(button="left")
                            self.d_delay = 1
                            # self.sound_delay = 1
                            self.d_clk_thread.start()



            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (20, 25), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            # cv2.imshow("camera", img)
            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def play_sound(self):
        playsound('G:\\A+\\College Project\\hand_tracking\\clickk.mp3')
        time.sleep(1)
        self.sound_delay = 0
        self.sound_thread = threading.Thread(target=self.play_sound)

    def l_clk_delay(self):
        time.sleep(1)
        self.l_delay = 0
        self.l_clk_thread = threading.Thread(target=self.l_clk_delay)

    def p_clk_delay(self):
        time.sleep(0.2)
        self.p_delay = 0
        self.p_clk_thread = threading.Thread(target=self.p_clk_delay)

    def r_clk_delay(self):
        time.sleep(1)
        self.r_delay = 0
        self.r_clk_thread = threading.Thread(target=self.r_clk_delay)

    def d_clk_delay(self):
        time.sleep(1)
        self.d_delay = 0
        self.d_clk_thread = threading.Thread(target=self.d_clk_delay)



