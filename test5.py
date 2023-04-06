import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./image/lena.png",0)
img_ltb = cv2.blur(img,(9,9))
img_gauss = cv2.GaussianBlur(img,(9,9),0)
img_ltv = cv2.medianBlur(img,9)

cv2.imshow("img_ltb",img_ltb)
cv2.imshow("img_gauss",img_gauss)
cv2.imshow("img_ltv",img_ltv)

hist1 = cv2.calcHist([img_ltb],[0],None,[256],[0,256])
plt.plot(hist1)
hist2 = cv2.calcHist([img_gauss],[0],None,[256],[0,256])
plt.plot(hist2)
hist3 = cv2.calcHist([img_ltv],[0],None,[256],[0,256])
plt.plot(hist3)

# điều chỉnh độ tương phản
# img_ltb1 = cv2.equalizeHist(img_ltb)
# img_gauss1 = cv2.equalizeHist(img_gauss)
# img_ltv1 = cv2.equalizeHist(img_ltv)

# hist4 = cv2.calcHist([img_ltb1],[0],None,[256],[0,256])
# plt.plot(hist4)
# hist5 = cv2.calcHist([img_gauss1],[0],None,[256],[0,256])
# plt.plot(hist5)
# hist6 = cv2.calcHist([img_ltv1],[0],None,[256],[0,256])
# plt.plot(hist6)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
