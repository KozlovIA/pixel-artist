from unicodedata import decimal
import numpy as np
import statistics as stat
import math

temp = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12),  (13, 14, 15, 16)] 


temp[1] = (65, 3, 1)







print("all oke")
#print(type(rgb2hex(0, 128, 64)))
#print(hex2rgb(hex()))


x = hex(16)
#print(list(x[1:]).decode('hex'))


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def hex2fgb(hexcode):
    return tuple([int(hexcode[i:i+2], 16) for i in range(1, 7, 2)])


#sps2=[math.sin(i*math.pi/5+2) for i in range(100)]
#print(sps2)


#print(hex2fgb('#f32fab'))
#print(rgb2hex(243, 47, 171))

#print(int('f32fab', 16))

def hex2int(hexcode):
    return int(hexcode.replace('#', ''), 16)
import colors
color_database = list(colors.hex_colors.values())
number_of_colors = len(color_database)
int_color_database = []
for i in range(number_of_colors):
    int_color_database.append(hex2int(color_database[i]))

print(int_color_database)