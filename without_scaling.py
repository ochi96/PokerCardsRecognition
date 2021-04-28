<<<<<<< HEAD
import cv2
import numpy as np
#open the main image and convert it to gray scale image
main_image = cv2.imread('board_info/board_components/board_cards/3.png')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
retval, gray_image = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("main", gray_image)
#open the template as gray scale image

#Open template and get canny
template = cv2.imread('templates/3.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
retval, template = cv2.threshold(template, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("template", template)
(height, width) = template.shape[:2]

#match the template using cv2.matchTemplate
match = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
position = np.where(match >= threshold) #get the location of template in the image
for point in zip(*position[::-1]): #draw the rectangle around the matched template
   print(match)
   cv2.rectangle(main_image, point, (point[0] + width, point[1] + height), (0, 204, 153), 0)
cv2.imshow('Template Found', main_image)
=======
import cv2
import numpy as np
#open the main image and convert it to gray scale image
main_image = cv2.imread('board_info/board_components/board_cards/3.png')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
retval, gray_image = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("main", gray_image)
#open the template as gray scale image

#Open template and get canny
template = cv2.imread('templates/3.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
retval, template = cv2.threshold(template, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("template", template)
(height, width) = template.shape[:2]

#match the template using cv2.matchTemplate
match = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
position = np.where(match >= threshold) #get the location of template in the image
for point in zip(*position[::-1]): #draw the rectangle around the matched template
   print(match)
   cv2.rectangle(main_image, point, (point[0] + width, point[1] + height), (0, 204, 153), 0)
cv2.imshow('Template Found', main_image)
>>>>>>> c8a2bbf1ebb08bacc42db6e9f9cb620083c0fcb2
cv2.waitKey(0)