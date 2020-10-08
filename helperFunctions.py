from PIL import(
    Image,
    ImageFilter,
    ImageOps
)
import pytesseract
from matplotlib import pyplot as plt
import os
import sys
import zipfile


def displayImage(image, figureTitle): 
    plt.imshow(image, cmap='gray') # we set the keyword argument "cmap", which is the colormapping of our image to grayscale
    plt.axis('off') # axes are not helpful in this instance
    plt.title(figureTitle) # we'll use the title to remind us of any processing we did to our image 


def readTextAndPrint(image):
    text = pytesseract.image_to_string(
        image,
        lang='eng',
        config='--psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-')
    
    text = text.strip('\n')
    text = text.strip()
    print('The text on the image is being read as:', text)

    
def imageConvolution(file):
    img = Image.open(file)
    img = ImageOps.invert(img)
    imageWidth, imageHeight = img.size
    imagePixels = img.load()
    
    for y in range(0, imageHeight):
        for x in range(0, imageWidth):
            if imagePixels[x, y] > 40:
                imagePixels[x, y] = 255
            else:
                pass
    
    for y in range(0, imageHeight):
        for x in range(0, imageWidth):
            if imagePixels[x, y] <= 11:
                imagePixels[x, y] = 0
            else:
                pass
            
    img = img.filter(ImageFilter.MinFilter(size=3))
    img = img.filter(ImageFilter.MinFilter(size=5))
    
    return img

def checkTesseractPath():
    if pytesseract.pytesseract.tesseract_cmd == 'tesseract':
        from shutil import which
        if which('tesseract') is None and 'win' in sys.platform:
            try:
                user = os.getlogin()
                pytesseract.pytesseract.tesseract_cmd = r'C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe'.format(user) # this tesseract path on my Windows machine
            except Exception:
                print('You need to find the location of the tesseract executable and set "pytesseract.pytesseract.tesseract_cmd" to this location, before you can proceed')
        elif which('tesseract') is not None and 'win' not in sys.platform:
            pytesseract.pytesseract.tesseract_cmd = which('tesseract')
        else:
            print('You need to find the location of the tesseract executable and set "pytesseract.pytesseract.tesseract_cmd" to this location, before you can proceed')

def unzipImages():
    if os.path.exists(r'\images'):
        pass
    else:
        with zipfile.ZipFile('images.zip', "r") as zipGDB:
            zipGDB.extractall('images')