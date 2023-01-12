import cv2
import numpy

# draw a rectangle
rectangle = numpy.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
# cv2.imshow("Rectangle", rectangle)
print(rectangle.shape)

# draw a circle
circle = numpy.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
# cv2.imshow("Circle", circle)
print(circle.shape)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
# cv2.imshow("OR", bitwiseOr)

################################################

img1 = cv2.imread("./image/a.jpg",0)
imgR1 = cv2.resize(img1,(240,240))
img2 = cv2.imread("./image/n.jpg",0)
imgR2 = cv2.resize(img2,(240,240))
imgAnd = cv2.bitwise_and(imgR1,imgR2)
cv2.imshow("AND",imgAnd)

imgOr = cv2.bitwise_or(imgR1,imgR2)
cv2.imshow("OR",imgOr)
cv2.waitKey(0)