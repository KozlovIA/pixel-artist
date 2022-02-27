# Ковертирование изображения в пиксельное
# Изображение и изображениеЧтение изображений
from PIL import Image
from skimage import io
import numpy as np
import colors
import time
import math

start_time = time.time()

# чтение с файла
img_file2 = io.imread('memecat.jpg')


imageSize = img_file2.shape     # получение размерности в виде: [x, y, z], где z=4 это кол-во сторон что ли, я не понял
# далее запись в матрицу кортежей значений с цветами пикселей
pixels_list = []
for i in range(imageSize[0]):
    pixels_list.append([])
    for j in range(imageSize[1]):
        pixels_list[i].append(tuple(img_file2[j][i]))

# преобразование квадрата пикселей(n на n), в пиксели среднего значения цвета RGB
# причем цвета пикселей в формате RGB
n=8     # корень из кол-ва пикселей
pixels_list_edit = pixels_list
try:
    for i in range(0, imageSize[0], n):
        j=0
        while j<imageSize[1]:
            temp = []   #промежуточные пиксели
            for k in range(n):
                for l in range(n):
                    temp.append(pixels_list[i+k][j+l])  # Добавление промежуточных пикселей для расчета среднего значения
            # расчет среднего значения из кортежа цвета (r, g, b), отдельно средний по r, g и b
            red = 0; green = 0; blue = 0
            for k in range(len(temp)):
                red += temp[k][0]
                green += temp[k][1]
                blue += temp[k][2]
            red /= len(temp); green /= len(temp); blue /= len(temp)     # значения, очевидно, float, цвета же должны быть в int, далее преобразование

            for k in range(n):
                for l in range(n):
                    pixels_list_edit[i+k][j+l] = (int(red), int(green), int(blue))
            j+=n
except:
    print('pixel broken')


def rgb2hex(RGB):
    """RGB - RHB tuple"""
    return "#{:02x}{:02x}{:02x}".format(RGB[0], RGB[1], RGB[2])

def hex2rgb(hexcode):
    return tuple([int(hexcode[i:i+2], 16) for i in range(1, 7, 2)])

def hex2int(hexcode):
    return int(hexcode.replace('#', ''), 16)

def cos_dist(rgb, approximation):
    numerator = sum( [rgb[i]*approximation[i] for i in range(3)]   )
    denominator = math.sqrt( sum([rgb[i]**2 for i in range(3)] )) * math.sqrt( sum([approximation[i]**2 for i in range(3)] ))
    if denominator == 0:
        denominator = 0.01
    ratio = numerator/denominator
    if ratio > 1:
        ratio = 1
    return math.acos(ratio)

# Преобразование средних значений к ближайшему цвету из базы данных
color_database = list(colors.colors.values())
number_of_colors = len(color_database)
for i in range(imageSize[0]):
    for j in range(imageSize[1]):
        current_pixel = pixels_list_edit[i][j]  # текущий пиксель изображения в формате RGB
        color_index = 0    # индекс цвета, который должен заменить пиксель
        #расчет приближения
        dist = 1
        for k in range(number_of_colors):
            test_dist = cos_dist(current_pixel, color_database[k])
            if test_dist < dist:
                dist = test_dist
                color_index = k
            elif test_dist == dist:
                euclid_color_index = (current_pixel[0]-color_database[color_index][0])**2 + (current_pixel[1]-color_database[color_index][1])**2 + (current_pixel[2]-color_database[color_index][2])**2
                euclid_k = (current_pixel[0]-color_database[k][0])**2 + (current_pixel[1]-color_database[k][1])**2 + (current_pixel[2]-color_database[k][2])**2
                if euclid_color_index < euclid_k:
                    color_index=k
        pixels_list_edit[i][j] = color_database[color_index]
        


# преобразование из матрицы в список, для использования в функции putdata()
new_list = []
for i in range(0, imageSize[0]):
    for j in range(0, imageSize[1]):
        new_list.append(pixels_list_edit[i][j])


im = Image.new('RGB', (imageSize[0], imageSize[1]))
im.putdata(new_list)
im_rotate = im.rotate(-90)
im_flip = im_rotate.transpose(Image.FLIP_LEFT_RIGHT)
im_flip.save('test.png')


print("Программа завершена, с запуска прошло", round(time.time() - start_time, 2), "сек")