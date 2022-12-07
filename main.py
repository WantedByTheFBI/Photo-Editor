
from PIL import Image
imagetheywant = input("Which image do you want to edit?: ")
im = Image.open(imagetheywant)
def merge():
    w = max(im.size[0], watermark.size[0])
    h = max(im.size[1], watermark.size[1])
    im2 = Image.new("RGBA", (w, h))

    im2.paste(im)
    im2.paste(watermark)
    return im2
def invertcolour(): #inverts the colour of the image
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (255-t[0], 255-t[1], 255-t[2])
            im.putpixel(xy, t)
    im.show()
def blueredswap():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[1], t[0])
            im.putpixel(xy, t)
    im.show()
def bluegreenswap():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[0], t[2], t[1])
            im.putpixel(xy, t)
    im.show()
def greenblueredshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[2], t[0])
            im.putpixel(xy, t)
    im.show()

def blueredgreenshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[2], t[0], t[1])
            im.putpixel(xy, t)
    im.show()
def greenredswap():
    for x in range(0,im.size[0]):
        for y in range(0,im.size[1]):
            xy = (x, y)
            t = im.getpixel(xy)
            t = (t[1], t[0], t[2])
            im.putpixel(xy, t)
    im.show()
while True:
    colourstochange = input("would you like to invert the colours[i], swap blue and red [br], swap blue and green [bg], swap red and green[rg], or shift the rbg values [gbr] [brg]: ")
    if colourstochange == "i":
        invertcolour()
    if colourstochange == "br":
        blueredswap()
    if colourstochange == "bg":
        bluegreenswap()
    if colourstochange == "gr":
        greenredswap()
    if colourstochange == "gbr":
        greenblueredshift()
    if colourstochange == "brg":
        blueredgreenshift()
    stopper = input("Would you like to keep changing the colours or stop?: ")
    if stopper == "stop":
        break

watermark = Image.open("watermark.png")
im = merge()
im.show()
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