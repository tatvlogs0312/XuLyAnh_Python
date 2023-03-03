# b1

import cv2
import numpy as np

img = cv2.imread("./image/a.jpg")
img = cv2.resize(img,(640,480))

hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv)

c = 255 / np.log(1 + np.max(v))
v_log = c * (np.log(v + 1))
v_log = np.array(v_log, dtype = np.uint8)

hsv2 = cv2.merge([h,s,v_log])
rgb = cv2.cvtColor(hsv2,cv2.COLOR_HSV2RGB)

cv2.imshow("anh bien doi log", rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
