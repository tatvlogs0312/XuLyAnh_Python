import cv2
import numpy as np
import imutils

image = cv2.imread("./image/bar.jpg")

# c1
image_center = tuple(np.array(image.shape[1::-1])/ 2)
rot_mat = cv2.getRotationMatrix2D(image_center, 45, 1.0)
result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
cv2.imshow("code", result)

# c2
rotate = imutils.rotate(image,45)
cv2.imshow("rotate", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()