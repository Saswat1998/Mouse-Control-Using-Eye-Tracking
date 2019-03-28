import cv2
import numpy as np
import pyautogui
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    # img = cv2.imread("WIN_20170206_19_22_48_Pro.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    eyes = eye_cascade.detectMultiScale(gray)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        roi_color2 = img[ey:ey + eh, ex:ex + ew]
        circles = cv2.HoughCircles(roi_gray2, cv2.HOUGH_GRADIENT, 1, 200, param1=200, param2=1, minRadius=0,
                                   maxRadius=0)
        try:
            for i in circles[0, :]:
                print(i)
                # draw the outer circle
                cv2.circle(roi_color2, (i[0], i[1]), i[2], (255, 255, 255), 2)
                print("drawing circle")
                # draw the center of the circle
                cv2.circle(roi_color2, (i[0], i[1]), 2, (255, 255, 255), 3)

                pyautogui.moveTo(i[0]+50,i[1]+50)


        except Exception as e:
            print(e)
        cv2.imshow('img', img)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()