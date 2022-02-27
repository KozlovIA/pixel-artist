import numpy as np
import statistics as stat
import math


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def hex2fgb(hexcode):
    return tuple([int(hexcode[i:i+2], 16) for i in range(1, 7, 2)])


def hex2int(hexcode):
    return int(hexcode.replace('#', ''), 16)


colors = {
    #"Черный": (0,0,0),
    "Белый": (255, 255, 255),
    "Красный": (255,0,0),
    "Лайм":	(0,255,0),
    "Синий": (0,0,255),
    "Желтый": (255,255,0),
    "Голубой":  (0,255,255),
    "Пурпурный": (255, 0, 255),
    "Серебряный": (192, 192, 192),
    "Серый": (128, 128, 128),
    "Бордовый":	(128,0,0),
    "Оливковое": (128,128,0),
    "Зеленый":	(0,128,0),
    "Фиолетовый": (128,0,128),
    "Бирюзовый": (0,128,128),
    "Флот":	(0,0,128),
    "test": (50, 50, 0)

}

def cos_dist(rgb, approximation):
    numerator = sum( [rgb[i]*approximation[i] for i in range(3)]   )
    denominator = math.sqrt( sum([rgb[i]**2 for i in range(3)] )) * math.sqrt( sum([approximation[i]**2 for i in range(3)] ))
    return math.acos(numerator/denominator)


color_database = list(colors.values())
dist = 1; k = 0
test_color = (191, 198, 208)
for i in range(len(colors)):
    test_dist = cos_dist(test_color, color_database[i])
    if test_dist < dist:
        dist = test_dist
        k = i
    elif test_dist == dist:
        euclid_i = (test_color[0]-color_database[i][0])**2 + (test_color[1]-color_database[i][1])**2 + (test_color[2]-color_database[i][2])**2
        euclid_k = (test_color[0]-color_database[k][0])**2 + (test_color[1]-color_database[k][1])**2 + (test_color[2]-color_database[k][2])**2
        if euclid_i < euclid_k:
            k=i


print(color_database[k], k)




