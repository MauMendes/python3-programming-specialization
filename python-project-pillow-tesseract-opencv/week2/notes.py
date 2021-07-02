# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 09:42:37 2021

@author: mauricio mendes
"""

#from PIL import Image
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image = Image.open("test.png")
##image = Image.open("display.png")
#print("Image size = {} x {}".format(image.width, image.height))
##image.show()
#text = pytesseract.image_to_string(image)
#print(text)

##########################################################

#from PIL import Image
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image = Image.open("display.png")
#print("Image size = {} x {}".format(image.width, image.height))
#text = pytesseract.image_to_string(image)
#if len(text)>1:
#    print('Text Decoded: ' + text)
#else:
#    print('Couldnt decode any text!')

#basewidth = 600
#wpercent = (basewidth/float(image.size[0]))
##print(wpercent)
#hsize = int(float(image.size[1])*float(wpercent))
##print(hsize)

#image.show()
##resizing we can improve the OCR detection
#img = image.resize((basewidth,hsize))
#img.show()
#making it grey can also help
#img = img.convert('L')
#img.show()#

##image.show()
#text = pytesseract.image_to_string(img)
#if len(text)>1:
#    print('Text Decoded: ' + text)
#else:
#    print('Couldnt decode any text!')

##########################################################
#from PIL import Image
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image = Image.open("display.png").convert('1') # black and white
#image.show()

#def binarize(image_to_transform, threshold):
#    output_image = image_to_transform.convert("L")
#    for x in range(output_image.width):
#        for y in range(output_image.height):
#            if output_image.getpixel((x,y))<threshold:
#                output_image.putpixel((x,y), 0)
#            else:
#                output_image.putpixel((x,y), 255)    
#    return output_image

#image = Image.open("display.png")
#img = binarize(image, 0)
#img.show()
#img = binarize(image, 64)
#img.show()
#img = binarize(image, 127)
#img.show()
#img = binarize(image, 200)
#img.show()
#img = binarize(image, 250)
#img.show()

##########################################################
#from PIL import Image
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#image = Image.open("fossil.jpg")
#print("Image size: {} x {}".format(image.width, image.height))
#image.show()

#bounding box
#bounding_box = (0,0,1920,1280) #Left Top Bottom Right
#bounding_box = (750,250,1200,400) #Left Top Right Bottom
#title_image = image.crop(bounding_box)
#title_image.show()

#text = pytesseract.image_to_string(title_image)
#if len(text)>1:
#   print('Text Decoded: ' + text)
#else:
#    print('Couldnt decode any text!')


