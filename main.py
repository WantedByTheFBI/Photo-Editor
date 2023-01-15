from PIL import Image
imagefiletheywant = input("Which image do you want to edit?: ")  #they input the filename that they want to manipulate
im = Image.open(imagefiletheywant)  #it opens said image file and makes it an object
originalformat = im.format  # retains the format for when saving the image


def invertcolour():  #inverts the colour of the image
    for x in range(0, im.size[0]):  #loops through the image widthwise
        for y in range(0, im.size[1]):  #loops through the image lengthwise
            xy = (x, y)  #takes the coordinates of a given pixel as a tuple
            pixelpostinversion = (255-(im.getpixel(xy)[0]),255-(im.getpixel(xy)[1]),255-(im.getpixel(xy)[2]))  #gets the pixel from the coordinates and subtracts the current value of the red, green, and blue values from 255 to get the opposite colour
            im.putpixel(xy, pixelpostinversion)  #puts the pixel back, colour inverted
    im.show()


def blueredswap():  #swaps blue and red values of pixels in the image
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            pixelpostswap = (im.getpixel(xy)[2], im.getpixel(xy)[1], im.getpixel(xy)[0])  #rgb (0,1,2) -> bgr (2,1,0)
            im.putpixel(xy, pixelpostswap)
    im.show()


def bluegreenswap():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            pixelpostswap = (im.getpixel(xy)[0], im.getpixel(xy)[2], im.getpixel(xy)[1]) #rgb (0,1,2) -> rbg (0,2,1)
            im.putpixel(xy, pixelpostswap)
    im.show()


def greenredswap():
    for x in range(0,im.size[0]):
        for y in range(0,im.size[1]):
            xy = (x, y)
            pixelpostswap = (im.getpixel(xy)[1], im.getpixel(xy)[0], im.getpixel(xy)[2])   #rgb (0,1,2) -> grb (1,0,2)
            im.putpixel(xy, pixelpostswap)
    im.show()


def greenblueredshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            pixelpostshift = (im.getpixel(xy)[1], im.getpixel(xy)[2], im.getpixel(xy)[0])  #rgb (0,1,2) -> gbr (1,2,0)
            im.putpixel(xy, pixelpostshift)
    im.show()


def blueredgreenshift():
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            xy = (x, y)
            pixelpostshift = (im.getpixel(xy)[2], im.getpixel(xy)[0], im.getpixel(xy)[1])  #rgb (0,1,2) -> gbr (2,0,1)
            im.putpixel(xy, pixelpostshift)
    im.show()


def resizeimage():  #allows the user to resize the image to their preferred size
    print("Your image is currently this large (width, height): " + str(im.size))  #gives user a reference for how big of numbers to use
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
    elif changephoto.lower() == "re":
        im = resizeimage()
    elif changephoto.lower() == "ro":
        rotateangle = int(input("How many degrees would you like to rotate the image?: "))
        keepimageexpanded = input("Would you like the image to keep it's original dimensions(type \"False\") or use the new dimensions(type \"True\")? ")
        if keepimageexpanded.lower() == "true": im = im.rotate(rotateangle, 0, True)
        else: im = im.rotate(rotateangle, 0, False)
    if (input("would you like to keep editing the photo? \"yes\" or \"no\" ")).lower() == "no": break


im.show()  #shows them the image one last time before they save it

print("The following 2 questions are yes or no questions, please answer them with a simple \"yes\" or \"no\". ")  #clarifying what they need to input
saveimage = input("Would you like to save the image?: ")  #if they don't like the photo they don't have to save it
if saveimage.lower() == "yes":
    override = input("Would you like to save the image to a different file name? (so it doesn't overwrite the previous image): ")  #it's nice to keep an original copy of the photo if you want
    if override.lower() == "yes":
        imagefiletheywant = (input("Please input the new file name here (do not include a formating option): ")) + f".{originalformat}"  #adds the original format to the end as to not mess up later
    newformat = input("Would you like to change the image format(put your desired format type here, if you don't want to change the format, type in \"NO\")?: ")  #gives them the option to change to format
    if newformat.lower() == "no": im.save(imagefiletheywant)
    else: im.save((((imagefiletheywant[::-1])[imagefiletheywant[::-1].index(".") + 1:len(imagefiletheywant):])[::-1])+newformat)  #A roundabout way to remove the original formating and add the new formatting regardless of prior formating type