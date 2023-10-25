import cv2
import numpy as np

# Load the image
image = cv2.imread('colonca10.jpeg', cv2.IMREAD_COLOR)

# Normalize the image
normalized_image = image / 255.0

# Save the normalized image to a file
cv2.imwrite('norm_colonca10.jpeg', normalized_image)

# Display the normalized image
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
