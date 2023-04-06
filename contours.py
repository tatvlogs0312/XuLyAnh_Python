import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./image/b.jpg")
ims = cv2.resize(img, [640, 480]) # type: ignore

img_gray = cv2.cvtColor(ims, cv2.COLOR_BGR2GRAY)
thresh, ims1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
Icoppy = ims.copy()
ims2 = ims.copy()
ims3 = ims.copy()

contours, hierarchy = cv2.findContours(ims1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    cv2.drawContours(ims, contours, -1, 255, 3)

    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    min_index = np.argmin(areas)
    cnt = contours[max_index]

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(ims, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.drawContours(ims2, contours[max_index], -1, (0, 255, 255), 3)
    cv2.drawContours(ims3, contours[min_index], -1, (0, 255, 255), 3)

    mask = np.zeros((ims.shape[:2]), np.uint8)
    mask[y : y + h, x : x + w] = 255
    masked_img = cv2.bitwise_and(ims1, ims1, mask=mask)
    cv2.imshow("max", masked_img)
    filter_img = cv2.blur(masked_img, (5, 5))
    cv2.imshow("max1", masked_img)
    thresh, filter_img2 = cv2.threshold(filter_img, 150, 255, cv2.THRESH_OTSU)
    filter_img2 = cv2.blur(masked_img, (5, 5))
    cv2.imshow("max2", filter_img2)
    filter_img3 = cv2.blur(masked_img, (5, 5))
    cv2.imshow("max3", filter_img3)
    thresh, filter_img4 = cv2.threshold(filter_img3, 150, 255, cv2.THRESH_OTSU)
    cv2.imshow("max4", filter_img4)
    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.dilate(filter_img4, kernel, iterations=1)
    masked_img_final = cv2.bitwise_and(ims3, ims3, mask=erosion)
    cv2.imshow("masked_img_final", masked_img_final)
    cv2.putText(masked_img_final,"aaaaa",(20,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
    cv2.imshow("masked_img_final_text", masked_img_final)


# cv2.imshow("contours", ims)
# cv2.imshow("contours max", ims2)
# cv2.imshow("contours min", ims3)

cv2.waitKey(0)
cv2.destroyAllWindows()