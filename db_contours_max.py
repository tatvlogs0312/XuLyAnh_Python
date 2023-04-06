import cv2
import numpy as np

img = cv2.imread("./image/a.jpg")
img = cv2.resize(img, (640,480))
img_gray = cv2.imread("./image/a.jpg", 0)
img_gray = cv2.resize(img_gray, (640,480))
thresh, img1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("anh binary", img1)

img_2 = img.copy()
img_3 = img.copy()
img_4 = img.copy()
img_5 = img.copy()

contours, hierarchy = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) != 0:
    # Vẽ contour tìm đc lên hình gốc
    cv2.drawContours(img, contours, -1, 255, 3)

    #  tìm contour lớn nhất
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    min_index = np.argmin(areas)
    cnt = contours[max_index]
    # Vẽ hình bao quanh contours lớn nhất
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.drawContours(img, contours[max_index], -1, (0, 255, 255), 3)
    cv2.drawContours(img, contours[min_index], -1, (0, 255, 255), 3)
    
    mask = np.zeros(img.shape[:2],np.uint8)
    mask[y:y+h, x:x+w] = 255
    mask_img = cv2.bitwise_and(img1,img1,mask=mask)
    # cv2.imshow()
    
    filter_img = cv2.blur(mask_img, (5,5))
    # cv2.imshow()
    thresh, filter_img2 = cv2.threshold(filter_img,150,255,cv2.THRESH_OTSU)
    # cv2.imshow()
    

cv2.imshow("contours", img)
cv2.imshow("contours max", img_3)
cv2.imshow("contours min", img_4)


if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
