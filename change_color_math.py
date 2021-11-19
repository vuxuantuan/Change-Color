""" Xanh Duong, do vang tim"""

# RED = [255, 0, 0]
# GOLD = [255, 223, 0]
# Blue = [0, 0, 255]
# Purple = [128, 0, 128]
import cv2
import numpy as np
import config
red = np.array([255, 0, 0])
gold = np.array([255, 215, 0])
blue = np.array([0, 0, 255])
purple = np.array([128, 0, 128])

# change blue to gold

img = cv2.imread(config.img_blue)
img = img.astype(np.uint8)
# img = cv2.cvtColor(cv2.COLOR_BGR2RGB)
img2 = np.zeros((img.shape[0], img.shape[1], 3))
img2[:, :, 0] = img[:, :, 2]
img2[:, :, 1] = img[:, :, 1]
img2[:, :, 2] = img[:, :, 0]
cv2.imwrite(config.result_blue_to_gold, img2)

# change blue to green
img2[:, :, 0] = (img[:, :, 0] + 255) / 2
img2[:, :, 1] = img[:, :, 1]
img2[:, :, 2] = img[:, :, 2] / 2
cv2.imwrite(config.result_blue_to_green, img2)

# change blue to purple
img2[:, :, 0] = img[:, :, 1]
img2[:, :, 1] = img[:, :, 2]
img2[:, :, 2] = (img[:, :, 0] + 255) / 2
cv2.imwrite(config.result_blue_to_purple, img2)

# change blue to purple
img2[:, :, 0] = img[:, :, 1]
img2[:, :, 1] = img[:, :, 1]
img2[:, :, 2] = img[:, :, 0]
cv2.imwrite(config.result_blue_to_red, img2)

# change purple to red
img = cv2.imread(config.img_purple)
img = img.astype(np.uint8)
img2 = np.zeros((img.shape[0], img.shape[1], 3))

img2[:, :, 0] = img[:, :, 2] * 2
img2[:, :, 1] = img[:, :, 1]
img2[:, :, 2] = img[:, :, 0] * 2
cv2.imwrite(config.result_purple_to_red, img2)

# change purple to gray
img2[:, :, 0] = img[:, :, 0]
img2[:, :, 1] = img[:, :, 2]
img2[:, :, 2] = img[:, :, 1]
cv2.imwrite(config.result_purple_to_gray, img2)

# change purple to green
img2[:, :, 0] = img[:, :, 2]
img2[:, :, 1] = img[:, :, 1] * 2 - 255
img2[:, :, 2] = img[:, :, 0]
cv2.imwrite(config.result_purple_to_green, img2)

# change purple to gold
img2[:, :, 0] = img[:, :, 1]
img2[:, :, 1] = img[:, :, 2] + 40
img2[:, :, 2] = img[:, :, 0] + 40
cv2.imwrite(config.result_purple_to_gold, img2)

# change purple to red
print(img[int(img.shape[0] / 2), int(img.shape[1] / 2), 2])
print(img[int(img.shape[0] / 2), int(img.shape[1] / 2), 1])
print(img[int(img.shape[0] / 2), int(img.shape[1] / 2), 0])

img2[:, :, 0] = img[:, :, 2] / 2 + 255 / 2
img2[:, :, 1] = img[:, :, 1] - 255
img2[:, :, 2] = img[:, :, 0] * 2 - 255

print(img2[int(img2.shape[0] / 2), int(img2.shape[1] / 2), 0])
print(img2[int(img2.shape[0] / 2), int(img2.shape[1] / 2), 1])
print(img2[int(img2.shape[0] / 2), int(img2.shape[1] / 2), 2])
cv2.imwrite(config.result_purple_to_red, img2)
