import cv2

# Path to your image file
image_path = 'C://Users//USER//Desktop//duccati.png'

# Read the image from the specified path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
cv2.imshow('Original Image', image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()

