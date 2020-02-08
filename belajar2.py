import numpy
import cv2

img = cv2.imread('kisspng-circle-point-clip-art-5af7b4042a5ba7.8981648215261829161735.jpg',0)
buram = cv2.medianBlur(img, 5)

halus = cv2.cvtColor(buram, cv2.COLOR_GRAY2BGR)

pipit = cv2.HoughCircles(buram, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=20, minRadius=0, maxRadius=55)

for i in pipit [0,:]:
    print(i)
    cv2.circle(halus, (i[0],i[1]),i[2], (0,255,0), 1)
    cv2.circle(halus, (i[0], i[1]), 2, (0, 0, 255), 2)

cv2.imshow('output', halus)
cv2.waitKey(0)