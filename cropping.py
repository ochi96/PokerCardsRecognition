<<<<<<< HEAD

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files/Tesseract-OCR/tesseract.exe'

def separation():
    original_img=cv2.imread("data/8d_Td_Qd_3d_Jd_Ad_Ad.png")
    resized_image = cv2.resize(original_img, (800,800), interpolation = cv2.INTER_AREA)
    coordinate_set = [(485,314,636,522),(434,72, 573, 252),(274, 6, 407, 183),(118,13,260, 211),(46,187,182, 365),
    (60, 443, 187, 608),(118, 597, 252, 760),(281, 615, 417, 791),(434, 528, 573, 720), (229, 250, 416, 542)]
    for i in range(10):
        start_row,start_col, end_row, end_col = coordinate_set[i]
        cropped = resized_image[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/{}.png").format(i), cropped)
    pass

def board_info():
    original_img = cv2.imread('board_info/9.png')
    coordinate_set = [(31, 0 , 131, 290),(0, 0, 30, 290)]
    for i in range(2):
        start_row, start_col, end_row, end_col = coordinate_set[i]
        cropped = original_img[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/board_components/{}.png").format(i), cropped)
    pass

def divide_cards():
    original_img = cv2.imread('board_info/board_components/0.png')
    coordinate_set = [(0, 0, 98, 67),(3, 70, 96, 124),(0,123, 92, 179), (0, 179, 92, 233), (0, 231, 98, 288)]
    for i in range(5):
        start_row, start_col, end_row, end_col = coordinate_set[i]
        print(1)
        cropped = original_img[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/board_components/board_cards/{}.png").format(i), cropped)
    pass

def ocr_core(filename):
    img = cv2.imread(filename)    
    grayscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    retval, threshold_img = cv2.threshold(grayscaled, 127, 155, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('threshold_img.jpeg', threshold_img)
    text = pytesseract.image_to_string(threshold_img, config='-c tessedit_char_whitelist=$Pot0123456789QKJ: ')
    print('#')
    return text

'''separation()
board_info()
divide_cards()'''
=======

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files/Tesseract-OCR/tesseract.exe'

def separation():
    original_img=cv2.imread("data/8d_Td_Qd_3d_Jd_Ad_Ad.png")
    resized_image = cv2.resize(original_img, (800,800), interpolation = cv2.INTER_AREA)
    coordinate_set = [(485,314,636,522),(434,72, 573, 252),(274, 6, 407, 183),(118,13,260, 211),(46,187,182, 365),
    (60, 443, 187, 608),(118, 597, 252, 760),(281, 615, 417, 791),(434, 528, 573, 720), (229, 250, 416, 542)]
    for i in range(10):
        start_row,start_col, end_row, end_col = coordinate_set[i]
        cropped = resized_image[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/{}.png").format(i), cropped)
    pass

def board_info():
    original_img = cv2.imread('board_info/9.png')
    coordinate_set = [(31, 0 , 131, 290),(0, 0, 30, 290)]
    for i in range(2):
        start_row, start_col, end_row, end_col = coordinate_set[i]
        cropped = original_img[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/board_components/{}.png").format(i), cropped)
    pass

def divide_cards():
    original_img = cv2.imread('board_info/board_components/0.png')
    coordinate_set = [(0, 0, 98, 67),(3, 70, 96, 124),(0,123, 92, 179), (0, 179, 92, 233), (0, 231, 98, 288)]
    for i in range(5):
        start_row, start_col, end_row, end_col = coordinate_set[i]
        print(1)
        cropped = original_img[start_row:end_row,start_col:end_col]
        cv2.imwrite(("board_info/board_components/board_cards/{}.png").format(i), cropped)
    pass

def ocr_core(filename):
    img = cv2.imread(filename)    
    grayscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    retval, threshold_img = cv2.threshold(grayscaled, 127, 155, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('threshold_img.jpeg', threshold_img)
    text = pytesseract.image_to_string(threshold_img, config='-c tessedit_char_whitelist=$Pot0123456789QKJ: ')
    print('#')
    return text

'''separation()
board_info()
divide_cards()'''
>>>>>>> c8a2bbf1ebb08bacc42db6e9f9cb620083c0fcb2
print(ocr_core("board_info/board_components/board_cards/3.png"))