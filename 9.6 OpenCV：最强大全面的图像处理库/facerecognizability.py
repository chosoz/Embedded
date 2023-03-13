import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #//人脸的特征文件
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")  #//人眼的特征文件

img = cv2.imread('face1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)         #//转为灰度图片（Haar识别的是灰度下的特征）
faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #//识别人脸
print(" There are {} faces in the input image".format(len(faces)))  #//显示 识别到的人脸数
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  #//人脸上绘制矩形框
    #//在识别到的人脸上， 识别眼睛
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray) #//识别人眼
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) #//在人眼上绘制矩形框

cv2.imshow('img',img)
cv2.waitKey(3000)
