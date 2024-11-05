import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\ASDF\Pictures\sample.png")

# Create a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# Apply the kernel to the image
sharpened_image = cv2.filter2D(src=image, ddepth=-1, kernel=sharpen_kernel)

# Save and display the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
