
from PIL import Image
imagetheywant = input("Which image do you want to edit?: ")
im = Image.open(imagetheywant)
originalformat = im.format
#watermark = Image.open("watermark.png")

#def merge():
    #im2 = Image.new("RGBA", (im.size[0], im.size[1]))

    #im2.paste(im)
    #im2.paste(watermark)
    #return im2
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

def resizeimage():
    print("Your image is currently this large (width, height): " + str(im.size))
    resizingwidth = int(input("How wide do you want it to be resized?: "))
    resizingheight = int(input("How tall do you want it to be resized?: "))
    resizedimensions = (resizingwidth, resizingheight)
    return im.resize(resizedimensions)
while True:
    changephoto = input("Would you like to alter colours[C] or resize the image[RE] or rotate the image [RO]: ")
    if changephoto.lower() == "c":
        colourstochange = input("Would you like to invert the colours[i], swap blue and red [br], swap blue and green [bg], swap red and green[rg], or shift the rbg values [gbr] [brg]: ")
        if colourstochange == "i": invertcolour()
        if colourstochange == "br": blueredswap()
        if colourstochange == "bg": bluegreenswap()
        if colourstochange == "gr": greenredswap()
        if colourstochange == "gbr": greenblueredshift()
        if colourstochange == "brg": blueredgreenshift()
        stopper = input("Would you like to keep changing the colours or stop?: ")
        if stopper == "stop": break
    elif changephoto.lower() == "re":
        im = resizeimage()
    elif changephoto.lower() == "ro":
        rotateangle = int(input("How many degrees would you like to rotate the image?: "))
        keepimageexpanded = input("Would you like the image to keep it's original dimensions(type \"False\") or use the new dimensions(type \"True\")?")
        if keepimageexpanded.lower() == "true": keepimageexpanded = True
        else: keepimageexpanded = False
        im = im.rotate(rotateangle, keepimageexpanded)

#w = int(im.size[0]/2)
#h = int(im.size[0]/8)
#wh = (w, h)
#watermark = watermark.resize(wh)
#im = merge()
im.show()
saveimage = input("Would you like to save the image?: ")
if saveimage.lower() == "yes":
    im.save(imagetheywant, originalformat)
newformat = input("Would you like to change the image format(put your desired format type here, if you don't want to change the format, type in \"NO\")?: ")
if newformat == "JPEG" or newformat == "JPG":
    if im.format == "RGBA":
        im = im.convert('RGB')
    im.save(imagetheywant, "JPEG")
elif newformat.lower() != "no":
    im.save(imagetheywant, newformat)