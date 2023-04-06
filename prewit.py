import cv2
import numpy as np

img = cv2.imread("./image/a.jpg", 0)
img = cv2.resize(img, (640, 480))

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

img_prewitx = cv2.filter2D(img,-1,kernelx)
img_prewity = cv2.filter2D(img,-1,kernely)
img_prewit = img_prewitx + img_prewity

cv2.imshow("img_prewitx",img_prewitx)
cv2.imshow("img_prewity",img_prewity)
cv2.imshow("img_prewit",img_prewit)

cv2.waitKey(0)
cv2.destroyAllWindows()