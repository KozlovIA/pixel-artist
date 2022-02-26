# Ковертирование изображения в пиксельное
# Изображение и изображениеЧтение изображений
from PIL import Image
from skimage import io
import numpy as np
import colors

# чтение с файла
img_file2 = io.imread('smile_ball.png')


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

# Преобразование средних значений к ближайшему цвету из базы данных
color_database = list(colors.hex_colors.values())
number_of_colors = len(color_database)
int_color_database = []
for i in range(number_of_colors):
    int_color_database.append(hex2int(color_database[i]))
for i in range(imageSize[0]):
    for j in range(imageSize[1]):
        current_pixel = rgb2hex(pixels_list_edit[i][j])  # текущий пиксель изображения в формате hex
        current_pixel = hex2int(current_pixel)
        color_index = 0    # индекс цвета, который должен заменить пиксель
        proximity = abs(int_color_database[0] - current_pixel)    # целочисленное приближение к цвету из библиотеки
        #расчет приближения
        for k in range(1, number_of_colors):
            if proximity > abs(int_color_database[k] - current_pixel):
                proximity = abs(int_color_database[k] - current_pixel)
                color_index = k
        pixels_list_edit[i][j] = hex2rgb(color_database[color_index])
print(proximity)


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
