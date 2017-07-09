from PIL import Image as I
import csv

##file = 'C:\\Users\\Owner\\Desktop\\mork.png'
file = 'C:\\Users\\Owner\\Desktop\\Untitled.png'
file.replace('\\', '/')

image_list = [] ## initialize a blank list to hold the RGB pixels


i = I.open(file)    ## this is the image
i_rgb = i.convert('RGB') ## this is the image once it's been converted to RGB colors
i_rgb_wd = i.size[0] ## this holds the width of the image in pixels
i_rgb_ht = i.size[1] ## this holds the height of the image in pixels

print(i_rgb_wd, i_rgb_ht) ## for debugging, give the width and heigh of the image in pixels

for row in range(0, i_rgb_ht):
    for col in range(0, i_rgb_wd):
        r, g, b = i_rgb.getpixel((col, row))
        image_list.append([row, col, r, g, b])

print('image_list has been created')



##for row in range(len(image_list)):
##    red_row1 = image_list[1][3]
##    print(red_row1)
