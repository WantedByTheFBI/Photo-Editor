
from PIL import Image
def blend_value(under, over, a):
    return int((over*a + under*(255-a)) / 255)

def blend_rgba(under, over):
    return tuple([blend_value(under[i], over[i], over[3]) for i in (0,1,2)] + [255])

white = (255, 255, 255, 255)

im = Image.open("watermark.png")
p = im.load()
for y in range(im.size[1]):
    for x in range(im.size[0]):
        p[x,y] = blend_rgba(white, p[x,y])
p.save('watermark.jpg')