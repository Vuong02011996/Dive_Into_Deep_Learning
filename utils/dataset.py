import cv2

image = cv2.imread("/home/vuong/Downloads/lingard.jpeg")

image = cv2.resize(image, (400, 400))

cv2.imwrite("/home/vuong/Downloads/lingard1.jpeg", image)
