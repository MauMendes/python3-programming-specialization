# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:37:41 2021

@author: mauricio mendes
"""
#import PIL
#print(PIL.__version__)
#help(PIL)
#
#from PIL import Image
#help(Image.open)

##file = "image.jpg"
#image = Image.open(file)
#print(image)

#import inspect
#print("The type of the image" + str(type(image)))
#inspect.getmro(type(image))
#image.show()

#from IPython.display import display
#display(image)


##############################################

import PIL
from PIL import Image
#file = "image.jpg"
#image = Image.open(file)
#image.save("image2.png")

###############################################

#from PIL import ImageFilter
#image = image.convert('RGB')
#blured_image = image.filter(PIL.ImageFilter.BLUR)
#blured_image = image.filter(PIL.ImageFilter.BoxBlur(10))
#blured_image = image.filter(PIL.ImageFilter.CONTOUR)
#blured_image = image.filter(PIL.ImageFilter.EMBOSS)
#blured_image = image.filter(PIL.ImageFilter.EDGE_ENHANCE)
#blured_image = image.filter(PIL.ImageFilter.EDGE_ENHANCE_MORE)        
#blured_image = image.filter(PIL.ImageFilter.SHARPEN)       
#blured_image = image.filter(PIL.ImageFilter.SMOOTH)                                              
#blured_image.show()

################################################

image2 = Image.open("honey.jpg")
blured_image = image2.filter(PIL.ImageFilter.CONTOUR)
blured_image.show()
blured_image.save("honey.png")

################################################

#print("{} x {}".format(image.width, image.height))
#image2 = image.crop((1000,1000,3000,2000)) #left top right bottom
#blured_image = image2.filter(PIL.ImageFilter.CONTOUR)
#mage2.show()
#blured_image.show()
#blured_image.save("contour.png")

################################################
#import PIL
#from PIL import Image
#from PIL import ImageEnhance

#file = "image.jpg"
#image = Image.open(file)
#image = image.convert('RGB')
#image = image.crop((1000,500,3000,2000))#L T R B
#print("{} x {}".format(image.width, image.height))

#enhancer=ImageEnhance.Brightness(image)
#images=[]

#create 10 images with diferents brightnessese
#for i in range(0,10):
#    images.append(enhancer.enhance(i/10))
 
#create an image with 10 times the size of the first image
#first_image = images[0]
#contact_sheet = PIL.Image.new('RGB', (first_image.width, 10*first_image.height))
##print(contact_sheet)

#paste the enchanced images
#current_location = 0
#for img in images:
#    contact_sheet.paste(img, (0, current_location))
#    current_location += first_image.height   
#contact_sheet.show()

################################################
#new contact sheet 3 x 3
#first_image = images[0]
#contact_sheet = PIL.Image.new('RGB', (3*first_image.width, 3*first_image.height))
#x=0
#y=0

#for img in images[1:]:
#    contact_sheet.paste(img, (x,y))
#    if x+first_image.width == contact_sheet.width:
#        x = 0
#        y = y+first_image.height
#    else:
#        x += first_image.width
#        
#contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
#contact_sheet.show()




