# From https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/
# Import packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

DIGITS_LOOKUP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 1, 0): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
}

# Load the image
image = cv2.imread('example.jpg')

# Pre-process the image by resizing it,converting it to
# grayscal, blurring it, and computing an edge map
image = imutils.resize(image, height = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)

# find the contours in the edge map, then sort them by their
# size in descending order
contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]
contours = 

# print(type(contours).__name__)
# cv2.imshow('Image', contours)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




