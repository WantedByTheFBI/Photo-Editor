
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
def invertcolour(): #inverts the colour of the image
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (255-t[0], 255-t[1], 255-t[2])
            im.putpixel(xy, t)
def blueredswap():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[1], t[0])
            im.putpixel(xy, t)
def bluegreenswap():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[0], t[2], t[1])
            im.putpixel(xy, t)
def greenblueredshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[2], t[0])
            im.putpixel(xy, t)

def blueredgreenshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[0], t[1])
            im.putpixel(xy, t)
def greenredswap():
    for x in range(0,im.size[0]):
        for y in range(0,im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[0], t[2])
            im.putpixel(xy, t)
while True:
    colourstochange = input("would you like to invert the colours[I], swap blue and red [br], swap blue and green [bg], swap red and green[rg], or shift the rbg values [gbr] [brg]: ")
    if colourstochange.lower == "i":
        invertcolour()
    if colourstochange.lower == "br":
        blueredswap()
    if colourstochange.lower == "bg":
        bluegreenswap()
    if colourstochange.lower == "gr":
        greenredswap()
    if colourstochange.lower == "gbr":
        greenblueredshift()
    if colourstochange.lower == "brg":
        blueredgreenshift()
    stopper = input("Would you like to keep changing the colours or stop?: ")
    if stopper == "stop":
        break
im.show()

#watermark = Image.open("watermark.png")
#print(watermark.size)
#thumbnailsize = (im.size[0]/2, im.size[1]/2)
#watermarkthumbnail = watermark.copy()
#watermarkthumbnail.thumbnail(thumbnailsize)
#watermarkyesno = input("Would you like to watermark it?")
#if watermarkyesno.lower == "yes":
    #im = merge(im, watermarkthumbnail)