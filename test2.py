# b3

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./image/a.jpg",1)
img = cv2.resize(img,(640,480))

b,r,g = cv2.split(img)

img_b = cv2.equalizeHist(b)
img_r = cv2.equalizeHist(r)
img_g = cv2.equalizeHist(g)

hist1 = cv2.calcHist([img_b],[0],None,[256],[0,256])
plt.plot(hist1,color = 'b')

hist2 = cv2.calcHist([img_r],[0],None,[256],[0,256])
plt.plot(hist2,color = 'r')

hist1 = cv2.calcHist([img_g],[0],None,[256],[0,256])
plt.plot(hist1,color = 'g')

plt.show()

brg = cv2.merge([img_b,img_r,img_b])
gbr = cv2.merge([img_g,img_b,img_r])
rgb = cv2.merge([img_r,img_g,img_b])

hsv = cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)

cv2.imshow("brg",brg)
cv2.imshow("gbr",gbr)
cv2.imshow("rgb",rgb)
cv2.imshow("hsv",hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()