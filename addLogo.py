import cv2

logo = cv2.imread("./image/epu.png")
img = cv2.imread("./image/n.jpg")

logo_width = logo.shape[0]
logo_height = logo.shape[1]

img[0:logo_width, 0:logo_height] = logo

print(img[0:logo_width, 0:logo_height])
print(logo)

cv2.imshow("img",img)
cv2.waitKey(0)