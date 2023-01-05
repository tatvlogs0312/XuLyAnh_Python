import cv2

img = cv2.imread("image\\a.jpg")

witdh = img.shape[0]
height = img.shape[1]

print(img[20,30])

for x in range(witdh):
    for y in range(height):
        if img[x,y][2] > 150:
            img[x,y] = (0,0,0)
        else:
            img[x,y] = (255,255,255)
            
cv2.imwrite('image\\a2.jpg', img)
