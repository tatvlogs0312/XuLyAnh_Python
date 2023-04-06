import numpy as np
import cv2

img = cv2.imread('./image/a.jpg')
img = cv2.resize(img,(640,480))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh, img1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


if len(contours) != 0 :
    areas = [cv2.contourArea(c) for c in contours]

    max_index = np.argmax(areas)
    cv2.drawContours(img, contours[max_index], -1, (0, 255, 255), 3)

    cv2.putText(img,str(contours[max_index].shape[0]),(20,10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
    cv2.putText(img,str(cv2.arcLength(contours[max_index],True)),(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))

    cv2.imshow("img",img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()