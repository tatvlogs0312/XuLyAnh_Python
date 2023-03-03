import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("./image/a.jpg",0)
img = cv2.resize(img,(640,480))
img_equalization = cv2.equalizeHist(img)
cv2.imshow("img",img)
cv2.imshow("img_equalization",img_equalization)

hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist1,color = 'b')

hist2 = cv2.calcHist([img_equalization],[0],None,[256],[0,256])
plt.plot(hist2,color = 'r')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()