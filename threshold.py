import cv2

img = cv2.imread("./image/a.jpg")
ret,thresh1 = cv2.threshold(img,255,255,cv2.THRESH_BINARY_INV)

imgWhite = cv2.resize(thresh1,(200,200))

cv2.imshow("ảnh",imgWhite)
cv2.waitKey(0)