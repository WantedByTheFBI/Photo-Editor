from PIL import Image
imagetheywant = input("Which image do you want to edit")
def merge(im1, im2):
    w = max(im1.size[0], im2.size[0])
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, 240)
    return im
def invertcolour(imagewidth, imageheight): #inverts the colour of the image
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (255-t[0], 255-t[1], 255-t[2])
            im.putpixel(xy, t)
im = Image.open(imagetheywant)
print(im.format, im.size, im.mode)
imagedimensions = list(im.size)
imagewidth = imagedimensions[0]
imageheight = imagedimensions[1]
if (input("Would you like to invert the colour of the image? ")).lower == "yes":
    invertcolour(imagewidth, imageheight)
watermark = Image.open("watermark.png")
watermarkthumbnail = watermark.copy()
watermarkthumbnail.thumbnail()
watermarkyesno = input("Would you like to watermark it?")
if watermarkyesno.lower == "yes":
    im = merge(im, watermark.thumbnail)
im.show(imagetheywant)

