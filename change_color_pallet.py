import cv2
import numpy as np
from change_color_function import *


# "red":0, "yellow":1, "blue":2, "purple":3, "black":4
def change_of_color_pallet(img_pallet, color_id_1, color_id_2):
    img_pallet = img_pallet.astype(np.uint8)
    img_result = np.zeros((img_pallet.shape[0], img_pallet.shape[1], 3))
    # input is red
    if color_id_1 == 0:
        # output is gold
        if color_id_2 == 1:
            pass
        # output is blue
        if color_id_2 == 2:
            pass
        # output is purple
        if color_id_2 == 3:
            pass
    # input is gold
    elif color_id_1 == 1:
        # output is red
        if color_id_2 == 0:
            pass
        # output is blue
        if color_id_2 == 2:
            pass
        # output is purple
        if color_id_2 == 3:
            img_result = change_gold_to_purple(img_pallet)
    # input is blue
    elif color_id_1 == 2:
        # output is red
        if color_id_2 == 0:
            img_result = change_blue_to_red(img_pallet)
        # output is gold
        if color_id_2 == 1:
            img_result = change_blue_to_gold(img_pallet)
        # output is purple
        if color_id_2 == 3:
            img_result = change_blue_to_purple(img_pallet)
    # input is purple
    elif color_id_1 == 3:
        # output is red
        if color_id_2 == 0:
            img_result = change_purple_to_red(img_pallet)
        # output is gold
        if color_id_2 == 1:
            img_result = change_purple_to_gold(img_pallet)
        # output is blue
        if color_id_2 == 2:
            img_result = change_purple_to_red(img_pallet)
    return img_result
