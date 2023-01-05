import cv2

img = cv2.imread("image\\n.jpg")
img2 = cv2.transpose(img)

cv2.imshow("1",img)
cv2.imshow("2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows