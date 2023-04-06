import numpy as np
import cv2

ims = cv2.imread('./image/bar.jpg')
img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
thresh, ims1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

kernel2 = np.ones((5,5), dtype=np.uint8)
i_erode = cv2.erode(img_gray,kernel2,iterations=1)
i_erode = cv2.erode(ims1,kernel2,iterations=1)
i_erode = cv2.erode(ims1,kernel2,iterations=1)
i_erode = cv2.erode(ims1,kernel2,iterations=1)
i_erode = cv2.erode(ims1,kernel2,iterations=1)
cv2.imshow("Idilate",i_erode)



cv2.waitKey(0)
cv2.destroyAllWindows()