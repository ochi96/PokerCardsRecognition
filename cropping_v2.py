import cv2
import re
from PIL import Image
import os
import pytesseract
from predict import predict_suit
from pixel_average import predict_suit_color

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files/Tesseract-OCR/tesseract.exe'

def board_info(filename):
    original_img = cv2.imread(filename)
    resized_image = cv2.resize(original_img, (1880,1300), interpolation = cv2.INTER_AREA)
    cropped = resized_image[429:585,640:1261]
    coordinate_set = [(0,126),(126, 250),(250,376),(376,502),(492,630)]
    for i in range(5):
        start_col, end_col = coordinate_set[i]
        card = cropped[0:161,start_col:end_col]
        cv2.imwrite(("board_state_cards/{}.png").format(i), card)
    board_cards = []
    for i in os.listdir('board_state_cards'):
        card = cv2.imread('board_state_cards/{}'.format(i))
        rank = ocr_rank_board(card)
        rank = re.sub(r'[^\w]', '', rank)#removes anything not a number, letter or underscore
        if rank == '':
            break
        cv2.imwrite('card.png', card)
        suit = predict_suit('card.png')
        board_cards.append(rank+suit)
    return board_cards

def ocr_rank_board(img):
    grayscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold_img = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    rank = threshold_img[0:50,0:47]
    cv2.imwrite('board_rank_threshold_img.jpeg', rank)
    text = pytesseract.image_to_string(rank, config='--psm 7 -c tessedit_char_whitelist=A0123456789QKJ')
    #print('Rank:', text)
    return text

def ocr_rank_player(img):
    grayscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold_img = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    rank = threshold_img[0:50,0:45]
    cv2.imwrite('player_rank_threshold_img.jpeg', rank)
    text = pytesseract.image_to_string(rank, config='--psm 7 -c tessedit_char_whitelist=A0123456789QKJ')
    #print('Rank:', text)
    return text

def ocr_pot_value(filename):
    img = cv2.imread(filename)
    resized_image = cv2.resize(img, (1880,1300), interpolation = cv2.INTER_AREA)
    cropped = resized_image[385:431,793:1097]
    grayscaled = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(grayscaled, 127, 155, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite('pot_value_threshold_img.jpeg', ~threshold_img)
    text = pytesseract.image_to_string(~threshold_img, config='--psm 7 -c tessedit_char_whitelist=$0123456789.')
    #print('Pot_value:', text)
    return text

def player_states(filename):
    original_img = cv2.imread(filename)
    resized_image = cv2.resize(original_img, (1880,1300), interpolation = cv2.INTER_AREA)
    #cv2.imwrite('trial.png',resized_image)
    coordinate_set = [(797, 731, 1027, 1237), (709, 173, 940, 640),(431, 17, 655, 455), (179, 77, 437, 517), 
    (80, 440, 320, 920), (80, 1030, 310, 1450), (187, 1407, 415, 1809), (460, 1389, 725, 1875), (687, 1213, 953, 1743)]
    for i in range(9):
        start_row,start_col, end_row, end_col = coordinate_set[i]
        cropped = resized_image[start_row:end_row,start_col:end_col]
        cv2.imwrite(("player_states/{}.png").format(i), cropped)
    pass

def user_info(filename):
    original_image = cv2.imread(filename)
    cropped_stack = original_image[142:200,0:290]
    grayscaled = cv2.cvtColor(cropped_stack, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(grayscaled, 127, 155, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite('stack_amount_threshold_img.jpeg', ~threshold_img)
    text = pytesseract.image_to_string(~threshold_img, config='--psm 7 -c tessedit_char_whitelist=$0123456789.')
    text_clean = re.sub(r'[^\w]', '', text)
    user_cards = []
    if text_clean != '':
        cropped_cards = original_image[8:87,96:328]
        coordinate_set = [(0,120),(120, 240)]
        for i in range(2):
            start_col, end_col = coordinate_set[i]
            card = cropped_cards[0:78,start_col:end_col]
            cv2.imwrite(("player_states/user_cards/{}.png").format(i), card)
            rank = ocr_rank_player(card)
            rank = re.sub(r'[^\w]', '', rank)
            if rank == '':
                break
            cv2.imwrite('card.png', card)
            suit = predict_suit_color('card.png')
            user_cards.append(rank+suit)
        print('user_stack_amount:', text)
        print('user_cards:', user_cards)
    else:
        print('No user present')
    pass

print('board_cards: ',board_info('data/Ad_Qd_3d_Qd_Td_9d_6c.png'))
print('pot_value: ',ocr_pot_value('data/Ad_Qd_3d_Qd_Td_9d_6c.png'))
player_states('data/Ad_Qd_3d_Qd_Td_9d_6c.png')
user_info('player_states/0.png')






