import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./image/lena.png",0)
cv2.imshow("goc",img)

s = [(3,3),(5,5),(7,7),(9,9)]
i = 1
for k in s:
    img_mean = cv2.blur(img,k)
    cv2.imshow(f'Anh trung binh {i}',img_mean)
    i = i + 1
    
img_mean1 = cv2.blur(img,(9,9))
gamma = 1.8
img_constr = np.power(img_mean1,gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr/max_val * 255
img_constr = img_constr.astype(np.uint8)

img_his = cv2.equalizeHist(img_mean1)
cv2.imshow("his",img_his)

cv2.waitKey(0)
cv2.destroyAllWindows()