import cv2

img = cv2.imread("./image/a.jpg",1)
b,g,r = cv2.split(img)
# cv2.imshow("img",img)
L = 25
# img_neg = 255 - img - L
# cv2.imshow("ảnh âm bản",img_neg)

b_neg = 255 - b - L
g_neg = 255 - g - L
r_neg = 255 - r - L

img_neg_merge_1 = cv2.merge([b_neg,g_neg,r_neg])
img_neg_merge_2 = cv2.merge([g_neg,b_neg,r_neg])
img_neg_merge_3 = cv2.merge([r_neg,g_neg,b_neg])

cv2.imshow("img1",img_neg_merge_1)
cv2.imshow("img2",img_neg_merge_2)
cv2.imshow("img3",img_neg_merge_3)


cv2.waitKey(0)
cv2.destroyAllWindows() 