import cv2
import numpy as np

img = cv2.imread("./image/a.jpg")
img = cv2.resize(img, (540,480))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((3,3),np.uint8)
IEdge = cv2.Canny(gray,170,255)
cv2.imshow("IEdge",IEdge)

kernel1 = np.ones((3,3), dtype=np.uint8)
IClosing = cv2.morphologyEx(IEdge,cv2.MORPH_CLOSE,kernel)
cv2.imshow("IClosing",IClosing)

kernel2 = np.ones((2,2), dtype=np.uint8)
Ierose = cv2.erode(IEdge,kernel2,iterations=1)
cv2.imshow("Ierose",Ierose)

Idilate = cv2.dilate(IEdge,kernel2,iterations=1)
cv2.imshow("Idilate",Idilate)


cv2.waitKey(0)
cv2.destroyAllWindows()