
from PIL import Image
imagetheywant = input("Which image do you want to edit?: ")
im = Image.open(imagetheywant)
if im.format != "JPG":
    YesToFileConvert = input("Would you like to convert the file to jpg?: ")
    print(im.mode)
    imagetheywant = imagetheywant[0:len(imagetheywant) - 3] + "jpg"
    im.save(imagetheywant, "JPEG")
    if YesToFileConvert.lower == "yes":
        im = im.convert('RGB')
        imagetheywant = imagetheywant[0:len(imagetheywant)-3] + "jpg"
        im.save(imagetheywant, "JPEG")
        print(im.format, im.size, im.mode)

#def merge(im1, im2):
    #w = max(im1.size[0], im2.size[0])
    #h = max(im1.size[1], im2.size[1])
    #im = Image.new("RGBA", (w, h))

    #im.paste(im1)
    #im.paste(im2, 240)
    #return im
def invertcolour(imagewidth, imageheight): #inverts the colour of the image
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (255-t[0], 255-t[1], 255-t[2])
            im.putpixel(xy, t)
def blueredswap(imagewidth,imageheight):
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[1], t[0])
            im.putpixel(xy, t)
def bluegreenswap(imagewidth, imageheight):
    for x in range(0, imagewidth):
        for y in range(0, imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[0], t[2], t[1])
            im.putpixel(xy, t)
def greenblueredshift(imagewidth, imageheight):
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[2], t[0])
            im.putpixel(xy, t)

def blueredgreenshift(imagewidth, imageheight):
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[0], t[1])
            im.putpixel(xy, t)
def greenredswap(imagewidth, imageheight):
    for x in range(0,imagewidth):
        for y in range(0,imageheight):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[0], t[2])
            im.putpixel(xy, t)
imagedimensions = list(im.size)
imagewidth = imagedimensions[0]
imageheight = imagedimensions[1]

invertcolour(imagewidth, imageheight)
#blueredswap(imagewidth, imageheight)
#bluegreenswap(imagewidth, imageheight)
#greenredswap(imagewidth, imageheight)
#greenblueredshift(imagewidth, imageheight)
#blueredgreenshift(imagewidth, imageheight)
im.show()

#watermark = Image.open("watermark.png")
#print(watermark.size)
#thumbnailsize = (im.size[0]/2, im.size[1]/2)
#watermarkthumbnail = watermark.copy()
#watermarkthumbnail.thumbnail(thumbnailsize)
#watermarkyesno = input("Would you like to watermark it?")
#if watermarkyesno.lower == "yes":
    #im = merge(im, watermarkthumbnail)