import cv2
import numpy as np

img = cv2.imread("./image/a.jpg")
imgResize = cv2.resize(img,(640,480))
print("Kênh màu " + str(img.shape[2]))
print("Chiều dài " + str(img.shape[1]))
print("Chiều rộng " + str(img.shape[0]))
# cv2.imshow("img",img)

# cv2.imshow("imgResize",imgResize)

# COLOR_BGR2GRAY là cờ chuyển
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_RGB2GRAY)
# cv2.imshow("imgGray",imgGray)

# Tạo ảnh nhị phân
ret,binary = cv2.threshold(imgGray,100,255,cv2.THRESH_OTSU)
print(binary.shape)
print(ret)

# cv2.imshow("binary",binary)

# RGB => HSV
imgHSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
# cv2.imshow("imgHSV",imgHSV)

# b,r,g = cv2.split(imgResize)
# cv2.imshow("blue",b)
# cv2.imshow("red",r)
# cv2.imshow("green",g)

h,s,v = cv2.split(imgHSV)
# cv2.imshow("h",h)
# cv2.imshow("s",s)
# cv2.imshow("v",v)

imgHSV2 = np.zeros((1038, 1845), dtype='uint8')
imgHSV2[:,:] = h*0.2 + s*0.5 + v*0.3
print(imgHSV2)
# cv2.imshow("imgHSV2",imgHSV2)

imgMerge = np.zeros((imgHSV.shape[:2]), dtype = 'uint8')
imgMerge = cv2.merge((h*0.2,s*0.5,v*0.3))
# imgMerge = cv2.merge([h,s,v])
cv2.imshow("imgMerge",imgMerge)

cv2.waitKey(0)
cv2.destroyAllWindows()