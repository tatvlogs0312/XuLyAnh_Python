import cv2
import numpy as np
img = cv2.imread("./image/d.jpg")
ims = cv2.resize(img, (640, 480))

c = 255 / np.log(1 + np.max(ims))
img_log = c * (np.log(ims + 1))
img_log = np.array(img_log, dtype = np.uint8)

cv2.imshow("img", ims)
cv2.imshow("anh bien doi log", img_log)

cv2.waitKey(0)
cv2.destroyAllWindows()