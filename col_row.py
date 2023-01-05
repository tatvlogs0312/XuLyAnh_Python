import cv2

img = cv2.imread("image\\n.jpg")

# in tất cả điểm ảnh theo hàng
print(f"row: {img[20:]}")

# in tất cả điểm ảnh theo cột
print(f"col: {img[:20]}")