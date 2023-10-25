import cv2
import numpy as np

# Load the image
image = cv2.imread('colonca10.jpeg', cv2.IMREAD_COLOR)

# Apply Gaussian blur for noise reduction
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Convert the blurred image to grayscale
gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# Enhance contrast in the grayscale image using histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Convert the equalized grayscale image back to BGR color format
enhanced_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)

# Display the enhanced image
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the enhanced image to a file
cv2.imwrite('enhanced_image.png', enhanced_image)


#mala mahit nhi ki image la aapn B/W madhe convert kea pahije ki nahi, please review it