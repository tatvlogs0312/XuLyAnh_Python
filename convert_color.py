import cv2

img = cv2.imread("image\\n.jpg")

# cvtColor() => đổi hệ màu
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('nga',img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows