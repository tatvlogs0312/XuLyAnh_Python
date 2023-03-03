import cv2
import numpy as np

# Load an image in BGR format
img = cv2.imread('./image/a.jpg')
img = cv2.resize(img, (640,480))

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Split the image into separate channels
h, s, v = cv2.split(hsv_img)

# Create a linear transformation matrix to increase the brightness of V channel
brightness_increase_matrix = 1.3 * np.ones_like(v)

# Apply the linear transformation to the V channel using cv2.multiply()
v_bright = cv2.multiply(v, brightness_increase_matrix)

# Merge the channels back into an HSV image
hsv_img_bright = cv2.merge([h, s, v_bright])

# Convert the image back to RGB color space
bright_img = cv2.cvtColor(hsv_img_bright, cv2.COLOR_HSV2RGB)


# Display the original and brightness increased image
cv2.imshow('Brightness Increased Image', bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()