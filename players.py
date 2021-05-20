import cv2
import numpy as np
import os
import re
from numpy.linalg import norm
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files/Tesseract-OCR/tesseract.exe'

def folded_or_non_folded(path='player_states/players/'):
    non_folded_players = []
    for image_name in os.listdir(path):
        img = cv2.imread('{}/{}'.format(path,image_name))
        img_no, ext = image_name.rsplit('.',1)
        if int(img_no)<=4:
            img = img[:,0:275]
        elif int(img_no)>4:
            img = img[:,150:]
        cv2.imwrite('player_states/cropped_players/{}.jpg'.format(img_no), img)
        if len(img.shape) == 3:
            brightness = np.average(norm(img, axis=2)) / np.sqrt(3)
            print(image_name, brightness)
            if brightness>45:
                non_folded_players.append(image_name)
    return non_folded_players

def bet_info(non_folded_players, path_to_folder='player_states/bets'):
    for item in os.listdir(path_to_folder):
        print(item)
        if item not in non_folded_players:
            os.remove('{}/{}'.format(path_to_folder,item))
    print(os.listdir(path_to_folder))
    for item in os.listdir(path_to_folder):
        text = ocr_bet_value('{}/{}'.format(path_to_folder,item))
        text_clean = re.sub(r'[^\w]', '', text)
        if text_clean == '':
            print('No bet')
        else:
            print(text_clean)
    pass

def player_states(filename):
    original_img = cv2.imread(filename)
    resized_image = cv2.resize(original_img, (1880,1300), interpolation = cv2.INTER_AREA)
    #cv2.imwrite('trial.png',resized_image)
    coordinate_set = [(797, 731, 1027, 1237), (709, 173, 940, 640),(431, 17, 655, 455), (179, 77, 437, 517), 
    (80, 440, 320, 920), (80, 1030, 310, 1450), (187, 1407, 415, 1809), (460, 1389, 725, 1875), (687, 1213, 953, 1743)]
    for i in range(9):
        start_row,start_col, end_row, end_col = coordinate_set[i]
        cropped = resized_image[start_row:end_row,start_col:end_col]
        cv2.imwrite(("player_states/players/{}.png").format(i), cropped)
    pass
    coordinate_set_bets = [(725,840,785,987), (680,541,775,737), (605,411,655,555), (371,451,440,593), (300,717,359,850),
    (259,1073,333,1223), (325,1281,409,1423), (561,1330,647,1489), (671,1171,740,1333)]
    for item in os.listdir('player_states/bets'):
        os.remove('player_states/bets/{}'.format(item))
    for i in range(9):
        start_row, start_col, end_row, end_col = coordinate_set_bets[i]
        card = resized_image[start_row:end_row, start_col:end_col]
        cv2.imwrite(("player_states/bets/{}.png").format(i), card)
    pass

def ocr_bet_value(filename):
    img = cv2.imread(filename)
    img_no = os.path.basename(filename)
    img_no, ext = img_no.rsplit('.',1)
    if int(img_no)<5:
        img = img[:,36:]
    elif int(img_no)>5:
        img = img[:,:-52]
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(grayscaled, 115, 155, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imwrite('bet_value_threshold_img.jpeg', ~threshold_img)
    text = pytesseract.image_to_string(~threshold_img, config='--psm 7 -c tessedit_char_whitelist=$0123456789.')
    #print('Pot_value:', text)
    return text

player_states('data/4h_Qh_6d_8d_Ac.png')
non_folded_players = folded_or_non_folded()
print(non_folded_players)
bet_info(non_folded_players=non_folded_players)

