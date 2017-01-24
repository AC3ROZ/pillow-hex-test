# -*- coding: utf-8 -*-

from PIL import Image
from collections import defaultdict

im = Image.open("NlarSMC.png")
hex_im = im.convert("RGB")
size = hex_im.size

count = defaultdict(int)


def rgb2hex(red, green, blue):
    return "#{red}{green}{blue}".format(red=(hex(red)[2:]),
                                        green=hex(green)[2:],
                                        blue=hex(blue)[2:])

for x in range(size[0]):
    for y in range(size[1]):
        count[rgb2hex(*hex_im.getpixel((x, y)))] += 1
