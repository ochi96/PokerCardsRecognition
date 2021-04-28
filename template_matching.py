<<<<<<< HEAD
import imutils
import cv2
import numpy as np

#Open template and get canny
template = cv2.imread('templates/3.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
retval, template = cv2.threshold(template, 175, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("template", template)
(height, width) = template.shape[:2]

#open the main image and convert it to gray scale image
main_image = cv2.imread('board_info/board_components/board_cards/3.png')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
retval, gray_image = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("main", gray_image)

temp_found = None
for scale in np.linspace(0.2, 0.5, 20)[::-1]:
   #resize the image and store the ratio
   resized_img = imutils.resize(gray_image, width = int(gray_image.shape[1] * scale))
   ratio = gray_image.shape[1] / float(resized_img.shape[1])
   if resized_img.shape[0] < height or resized_img.shape[1] < width:
      break
   #Convert to edged image for checking
   #e = cv2.Canny(resized_img, 10, 25)
   match = cv2.matchTemplate(resized_img, template, cv2.TM_CCOEFF)

   (_, val_max, _, loc_max) = cv2.minMaxLoc(match)
   if temp_found is None or val_max>temp_found[0]:
      temp_found = (val_max, loc_max, ratio)
#Get information from temp_found to compute x,y coordinate
(_, loc_max, ratio) = temp_found
(x_start, y_start) = (int(loc_max[0]), int(loc_max[1]))
(x_end, y_end) = (int((loc_max[0] + width)), int((loc_max[1] + height)))
#Draw rectangle around the template

cv2.rectangle(main_image, (x_start, y_start), (x_end, y_end), (0, 204, 153), 0)
cv2.imshow('Template Found', main_image)
=======
import imutils
import cv2
import numpy as np

#Open template and get canny
template = cv2.imread('templates/3.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
retval, template = cv2.threshold(template, 175, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("template", template)
(height, width) = template.shape[:2]

#open the main image and convert it to gray scale image
main_image = cv2.imread('board_info/board_components/board_cards/3.png')
gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
retval, gray_image = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("main", gray_image)

temp_found = None
for scale in np.linspace(0.2, 0.5, 20)[::-1]:
   #resize the image and store the ratio
   resized_img = imutils.resize(gray_image, width = int(gray_image.shape[1] * scale))
   ratio = gray_image.shape[1] / float(resized_img.shape[1])
   if resized_img.shape[0] < height or resized_img.shape[1] < width:
      break
   #Convert to edged image for checking
   #e = cv2.Canny(resized_img, 10, 25)
   match = cv2.matchTemplate(resized_img, template, cv2.TM_CCOEFF)

   (_, val_max, _, loc_max) = cv2.minMaxLoc(match)
   if temp_found is None or val_max>temp_found[0]:
      temp_found = (val_max, loc_max, ratio)
#Get information from temp_found to compute x,y coordinate
(_, loc_max, ratio) = temp_found
(x_start, y_start) = (int(loc_max[0]), int(loc_max[1]))
(x_end, y_end) = (int((loc_max[0] + width)), int((loc_max[1] + height)))
#Draw rectangle around the template

cv2.rectangle(main_image, (x_start, y_start), (x_end, y_end), (0, 204, 153), 0)
cv2.imshow('Template Found', main_image)
>>>>>>> c8a2bbf1ebb08bacc42db6e9f9cb620083c0fcb2
cv2.waitKey(0)