import cv2
import numpy as np

image1 = cv2.imread('Task_3.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 199, 5)

ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)
cv2.imshow('Binary Threshold', thresh3)

cv2.imwrite('Task3_Adaptive Mean.jpg', thresh1)
cv2.imwrite('Task3_Adaptive Gaussian.jpg', thresh2)
cv2.imwrite('Task3_simple_binary_threshold.jpg', thresh3)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()