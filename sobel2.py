import cv2

img = cv2.imread("./image/a.jpg", 0)
img = cv2.resize(img, (640, 480))

img_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
img_xy = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)

cv2.imshow("img_sobelx",img_x)
cv2.imshow("img_sobely",img_y)
cv2.imshow("img_sobel",img_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()