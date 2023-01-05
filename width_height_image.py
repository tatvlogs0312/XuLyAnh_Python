import cv2

img = cv2.imread("image\\n.jpg")
Pval = img[20,30]
# img.shape => lấy ra (width,height,kênh màu)
print(img.shape)
print(f"width : {img.shape[0]}")
print(f"height : {img.shape[1]}")
print(Pval)

center = img[int(img.shape[0]/2),int(img.shape[1]/2)]
print(center)

# thay đổi kích thước ảnh
img2 = cv2.resize(img,(540,540))

for i in range(540):
    # gán màu cho ảnh
    img2[0:50,i] = (0,255,0)
    
cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()