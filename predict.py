from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2

model = load_model('models/cards_model.h5')

def predict_suit(img):
    img = image.load_img(img, target_size=(126, 160), color_mode = 'grayscale')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)[0]
    suit = None
    if max(preds)==preds[0]:
        suit = 'c'
    if max(preds)==preds[1]:
        suit = 'd'
    if max(preds)==preds[2]:
        suit = 'h'
    if max(preds)==preds[3]:
        suit = 's'
    return suit

#print(predict_suit('board_info/1.png'))
