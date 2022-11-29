from PIL import Image
imagetheywant = input("Which image do you want to edit")

im = Image.open(imagetheywant)
im.show(imagetheywant)
print(im.format, im.size, im.mode)
imagedimensions = list(im.size)
imagewidth = imagedimensions[0]
imageheight = imagedimensions[1]
def invertcolour(imagewidth, imageheight): #inverts the colour of the image
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)

            t = (255-t[0], 255-t[1], 255-t[2])
            im.putpixel(xy, t)
invertcolour(imagewidth, imageheight)
im.show(imagetheywant)
def watermark(): #forces my watermark onto it
    w = max(im.size[0], watermark.size[0])
    h = max(im.size[1], watermark.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im)
    im.paste(watermark, (im.size[0], 0))

    return im