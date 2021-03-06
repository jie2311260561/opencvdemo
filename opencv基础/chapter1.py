import cv2
import numpy as np


img = cv2.imread("Picture\picture1.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=5)

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.waitKey(0)
# img = cv2.imread(r"D:\learn Java\pyday\opencvdemo\opencv基础\Picture\picture1.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)
# cap = cv2.VideoCapture(r"D:\learn Java\pyday\opencvdemo\opencv基础\Picture\10款MG流体特效火焰烟雾标题AE模板.mp4")
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break