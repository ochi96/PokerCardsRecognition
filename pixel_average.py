import cv2
import numpy as np
from statistics import mean

def predict_suit_color(img):
    img = cv2.imread(img)
    color_area = img[2:76,2:42]
    height, width, _ = np.shape(color_area)
    # calculate the average color of each row of our image
    avg_color_per_row = np.average(img, axis=0)
    # calculate the averages of our rows
    avg_colors = np.average(avg_color_per_row, axis=0)
    # avg_color is a tuple in BGR order of the average colors
    # but as float values
    #print(f'avg_colors: {avg_colors}')
    # so, convert that array to integers
    int_averages = np.array(avg_colors, dtype=np.uint8)
    #print(f'int_averages: {int_averages}')
    if max(int_averages)==int_averages[0]:
        suit = 'd'
    if max(int_averages)==int_averages[1]:
        suit = 'c'
    if max(int_averages)==int_averages[2]:
        suit = 'h'
    if mean(int_averages)==int_averages[0]:
        suit = 's'
    return suit

#print(predict_suit_color('player_states/user_cards/1.png'))

