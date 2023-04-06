import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./image/lena.png", 0)
# ims = cv2.resize(img, (800, 540))
cv2.imshow("anh goc", img)

img_gauss = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow("anh loc", img_gauss)

s = [(3, 3), (5, 5), (7, 7)]
for i, k in enumerate(s):
    img_gauss1 = cv2.GaussianBlur(img, k, 0)
    cv2.imshow(f"anh loc {i}", img_gauss1)


img_equalization = cv2.equalizeHist(img_gauss)
cv2.imshow("anh can bang hist", img_equalization)

gamma = 1.8
img_constr = np.power(img_gauss, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr / max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow(f"anh loc constr", img_constr)

cv2.waitKey(0)
cv2.destroyAllWindows()