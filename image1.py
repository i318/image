import os
import PIL
from PIL import Image
from PIL import ImageFilter

def openimg():
    image1 = Image.open(os.path.join('pictures', q1))


def bnw():
    bnwim = image1.convert('L')
    bnwim.show()
    

def rotation():
    amount = input(int("How much would you like to rotate the image?"))
    rotate0 = image1.rotate(amount)
    rotate0.show()
    Image.save('Image1edit.jpg')
  


def thumbnailsize():
        size = input(int(float("What size? Enter one number.")))
        ts = image1.thumbnail(size)
        ts.save('Image1edit.jpg')
        ts.show()

        

#im.save('C:\Users\Shania\Desktop\pythonhw\'pngs')

def blur():
    blurImage = image1.filter(ImageFilter.BLUR)
    blurImage.show()
    
def jpgtopng():
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i = Image.open(f)
            fn, fext,  = os.path.splitext(f)
            i.save('pngs/{}.png'.format(fn))



q1 = input("What image would you like to edit, including .[filetype]?")

if q1 == q1:
    image1 = Image.open(os.path.join('pictures', q1))
    image1.show()
    correct = input("Is this correct? y or n")
    if correct == 'y':
        edit1 = input("What would you like to do to this image? [Blur][bnw][rotate][convert to png(type n)][rotate][thumbnail]")
        if edit1 == 'bnw':
            bnw()
        elif edit1 == "n":
            jpgtopng()
        elif edit1 == "rotate":
            rotation()
        elif edit1 == "blur":
            blur()
        elif edit1 == "thumbnail":
            thumbnailsize()






def thumbnail_size():
    pass





#i should also save rotated photos to sep file
#     





#image1 = Image.open(os.path.join('pictures', 'aw.jpg'))
#image1.show()


