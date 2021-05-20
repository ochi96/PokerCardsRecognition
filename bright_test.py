from PIL import Image, ImageStat
import os
import cv2

'''
def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

def folded_or_non_folded(path='player_states/players/'):
    non_folded_players = []
    for image_name in os.listdir(path):
        img = Image.open('{}/{}'.format(path,image_name)).convert('L')
        img_no, ext = image_name.rsplit('.',1)
        if int(img_no)<=4:
            img = img[:,0:275]
        elif int(img_no)>4:
            img = img[:,:-252]
        stat = ImageStat.Stat(img)
        brightness = stat.mean[0]
        print(image_name, brightness)
        if brightness>55:
            non_folded_players.append(image_name)
    return non_folded_players

#print(brightness('player_states/players/3.png'))
folded_or_non_folded()
'''
img = cv2.imread("player_states/cropped_players/5.jpg")
img = img[0:130,:]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



ret, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

img[thresh == 255] = 0

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erosion = cv2.erode(img, kernel, iterations = 1)
cv2.imwrite('dimmed.jpg', erosion)
#cv2.destroyAllWindows()