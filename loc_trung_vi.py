import cv2
import numpy as np

img = cv2.imread("./image/lena.png")
cv2.imshow("goc",img)

img_median = cv2.medianBlur(img,9)
cv2.imshow("img_median",img)

cv2.waitKey(0)
cv2.destroyAllWindows()