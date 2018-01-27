# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:56:24 2018

@author: Peter Huang
"""

from PIL import Image

def _checkPixel(x, y, length, height):
    # check x to make sure it isn't beyond picture lengths, if it is, return false
    if (x < 0 or x >= length):
        return False
    
    # check y like x
    if (y < 0 or y >= height):
        return False
    
    return True

# load image to be smoothed
original = Image.open('me.jpg')

# figure out how much it needs to be cropped
blur = input('Type 5x5, 7x7, or 9x9: ')

print("You have chosen: " + blur + " blur")

# load factor into actual int
factor = 0;
if (blur == '5x5'):
    factor = 5
elif (blur == '7x7'):
    factor = 7
elif (blur == '9x9'):
    factor = 9;

print(factor)

# get length and width of picture
length, height = original.size

# create a new image with values initialized
new_pic = Image.new('RGB', (length, height), 'red')

# for each pixel
for y in range(0, height):
    for x in range(0, length):
        r_val = 0
        g_val = 0
        b_val = 0
        pixel_count = 0
        
        # calculate the sum of convolution of kernel with image of all pixels in kernel
        # for each rgb value
        for kernel_y in range(y - int(factor / 2), y + 1 +  int(factor / 2)):
            for kernel_x in range(x - int(factor / 2), x + 1 + int(factor / 2)):
                # check if pixel value we're getting is valid
                if (_checkPixel(x + kernel_x, y + kernel_y, length, height) == True):
                    # if it is, get each rgb val and increment it in our counter
                    r,g,b = original.getpixel((x + kernel_x, y + kernel_y))
                   
                    r_val += r
                    g_val += g
                    b_val += b
                    pixel_count += 1
        
        if (pixel_count == 0):
            pixel_count = 1
       
        # divide by sum of coefficients in kernel
        r_val = int(r_val / (pixel_count))
        g_val = int(g_val / (pixel_count))
        b_val = int(b_val / (pixel_count))
        
        # put newly calculated rgb value into new pic
        new_pic.putpixel((x,y), (r_val, g_val, b_val))
     
# save picture
new_pic.save('Huang_Peter_blurred.jpg')

                








