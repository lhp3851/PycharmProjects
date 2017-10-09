from PIL import Image

import os
import shutil

kPROJECT_DIR = os.getcwd()
kDESTINATION_PATH = kPROJECT_DIR + "/ios/Resource/"
imagePath = kPROJECT_DIR + "/ios/Resource/icon_1024x1024.png"
print(imagePath,kDESTINATION_PATH)
icon_image = Image.open(imagePath)
print(icon_image.format, icon_image.size, icon_image.mode)


def generateImageWithSize(size):
    imageName = kDESTINATION_PATH + str(size) + ".png"
    shutil.copy(imagePath, imageName)
    image = Image.open(imageName)
    new_image = image.resize((size, size))
    new_image.save(imageName)

for x in range(10):
    if x == 0:
        generateImageWithSize(57)
    if x == 1:
        generateImageWithSize(114)
    if x == 2:
        generateImageWithSize(29)
    if x == 3:
        generateImageWithSize(58)
    if x == 4:
        generateImageWithSize(87)
    if x == 5:
        generateImageWithSize(40)
    if x == 6:
        generateImageWithSize(80)
    if x == 7:
        generateImageWithSize(120)
    if x == 8:
        generateImageWithSize(180)
    if x == 9:
        generateImageWithSize(76)
    if x == 10:
        generateImageWithSize(152)


