import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import random

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector=HandDetector(detectionCon=0.8,maxHands=1)


class SnakeGameClass:
    def __init__(self,pathFood):
        self.points=[]
        self.lengths=[]
        self.currentLength=0
        self.allowedLength=150
        self.previousHead = 0,0
        self.imgFood=cv2.imread(pathFood,cv2.IMREAD_UNCHANGED)
        self.imgFood=cv2.resize(self.imgFood,(70,70))
        self.hFood,self.wFood,_=self.imgFood.shape
        self.foodPoint=0,0
        self.score=0
        self.scoreBuffer=0
        self.gameOver=False
        self.randomFoodLocation()

    def randomFoodLocation(self):
        self.foodPoint=random.randint(100,1000),random.randint(100,600)

    def update(self,imgMain,currentHead):

        if self.gameOver:
            cvzone.putTextRect(imgMain,"GameOver",(300,400),scale=7,thickness=5,offset=20)
            cvzone.putTextRect(imgMain,f'Your Score {self.scoreBuffer}',(300,550),scale=7,thickness=5,offset=20)
        else:
            px,py=self.previousHead
            cx,cy=currentHead

            self.points.append([cx,cy])
            distance=math.hypot(cx-px,cy-py)
            self.lengths.append(distance)
            self.currentLength+=distance
            self.previousHead=cx,cy
            #
            # lenght reduction
            #
            if self.currentLength>self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength-=length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength<self.allowedLength:
                        break
            # check if snake ate the food
            rx,ry=self.foodPoint
            if rx-self.wFood//2 <cx <rx+self.wFood//2 and ry-self.hFood//2 <cy <ry+self.hFood//2:
                self.randomFoodLocation()
                self.allowedLength+=50
                self.score+=1



            # draw snake
            if self.points:
                for i,point in enumerate(self.points):
                    if i!=0:
                        cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
                cv2.circle(img,self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            # draw Food
            rx,ry=self.foodPoint
            imgMain=cvzone.overlayPNG(imgMain,self.imgFood,(rx-self.wFood//2,ry-self.hFood//2))

            cvzone.putTextRect(imgMain, f'Score {self.score}', (100, 100), scale=5, thickness=2, offset=20)

            # check for collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            minDist=cv2.pointPolygonTest(pts,(cx,cy),True)
            # print(len(self.lengths))
            if -2<= minDist<= 2 and len(self.lengths)>20:
                self.gameOver=True
                self.points = []
                self.lengths = []
                self.currentLength = 0
                self.scoreBuffer=self.score
                self.score=0
                self.allowedLength = 150
                self.previousHead = 0, 0
                self.randomFoodLocation()

        return imgMain


game=SnakeGameClass('pngegg.png')

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)

    if hands:
        lmList=hands[0]['lmList']
        pointIndex=lmList[8][0:2]
        img=game.update(img,pointIndex)

    cv2.imshow("image",img)
    key=cv2.waitKey(1)
    if key==ord('r'):
        game.gameOver=False