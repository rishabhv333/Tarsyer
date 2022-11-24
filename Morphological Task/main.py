import cv2
import numpy as np

img = cv2.imread('Star_Wars_Logo.png', 0)
kernel = np.ones((5,5), np.uint8)
# cv2.imshow('Image', img)

erosion = cv2.erode(img, kernel)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.imwrite("Task_3_erosion.png",erosion)

dilation = cv2.dilate(img,kernel,iterations=3)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)
cv2.imwrite('task2_dilation.png', dilation)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)
cv2.imwrite("Task_3_blackhat.png", blackhat)