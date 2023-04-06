import cv2
import numpy as np

img = cv2.imread("./image/a.jpg", 0)
img = cv2.resize(img, (640, 480))

kernelx = np.array([[1,1,1],[-2,0,2],[-1,0,-1]])
kernely = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

img_sobelx = cv2.filter2D(img,-1,kernelx)
img_sobely = cv2.filter2D(img,-1,kernely)
img_sobel = img_sobelx + img_sobely

cv2.imshow("img_sobelx",img_sobelx)
cv2.imshow("img_sobely",img_sobely)
cv2.imshow("img_sobel",img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()