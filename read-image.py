import cv2

# doc anh tu thui muc
img = cv2.imread("image\\n.jpg")
# chinh kich thuoc anh
imS = cv2.resize(img, (540, 540))   
# hien thi anh len man hinh
cv2.imshow("nga",imS)
cv2.waitKey(0)
cv2.destroyAllWindows()