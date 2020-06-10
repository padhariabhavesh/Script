# @Bhavesh Padharia
# www.padharia.in/blog

# Convert image to black and white

import cv2
img_gray = cv2.imread("image path in png format", cv2.IMREAD_GRAYSCALE)
thres=128
img_b = cv2.threshold(img_gray,thres,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("blackwhite.png",img_b)

