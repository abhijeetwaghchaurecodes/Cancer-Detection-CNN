import cv2
import numpy as np

# Load the image
image = cv2.imread('colonca10.jpeg', cv2.IMREAD_COLOR)

# Normalize the image
normalized_image = image / 255.0

# Apply Gaussian blur for noise reduction
blurred_image = cv2.GaussianBlur(normalized_image, (5, 5), 0)

# Save the blurred image to a file
cv2.imwrite('blurred_image.jpeg', blurred_image)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
