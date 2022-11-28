import PIL.ImageColor
from PIL import Image
import os, sys
im = Image.open("GraphicDesignIsMyPassion.jpg")
im.show("GraphicDesignIsMyPassion.jpg")
print(im.format, im.size, im.mode)
def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

