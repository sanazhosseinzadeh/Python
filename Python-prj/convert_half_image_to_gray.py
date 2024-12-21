import cv2
import numpy as np

# Load the image
image = cv2.imread('dog.jpg')

# Get the dimensions of the image
height, width, _ = image.shape

# Split the image in half (vertically)
left_half = image[:, :width//2]
right_half = image[:, width//2:]

# Convert the right half to grayscale
right_half_gray = cv2.cvtColor(right_half, cv2.COLOR_BGR2GRAY)

# Convert grayscale back to 3 channels to match the original image's shape
right_half_gray = cv2.cvtColor(right_half_gray, cv2.COLOR_GRAY2BGR)

# Combine the left half (original) and the right half (grayscale)
combined_image = np.hstack((left_half, right_half_gray))

# Save or display the result
cv2.imwrite('half_image_grayscale.jpg', combined_image)
cv2.imshow('Half Grayscale Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()