import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./image/a.jpg")
ims = cv2.resize(img, [640, 480]) # type: ignore

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)

t_lower = 50
t_upper = 150

img_canny = cv2.Canny(img_gray, t_lower, t_upper, L2gradient=True)
cv2.imshow("Canny", img_canny)
cv2.imshow("anh goc", ims)


cv2.waitKey(0)
cv2.destroyAllWindows()