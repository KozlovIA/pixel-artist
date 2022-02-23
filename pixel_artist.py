# Ковертирование изображения в пиксельное
# Изображение и изображениеЧтение изображений
from PIL import Image
import os
from matplotlib import pyplot as plot
from skimage import io, transform
import numpy as np
import statistics as stat

# чтение с файла
#img_file1 = Image.open('smile_ball.png')
img_file2 = io.imread('Gerb.jpg')
# Размер данных после прочтения картинки:
#print ("the picture's size: ", img_file1.size)
#print ("the picture's shape: ", img_file2.shape)

# Получить пиксели:
#print(img_file1.getpixel((500,500)), img_file2[500][500])
#print(img_file2[10][10])

#img1 = Image.new("RGB", (100, 100))
#img1.show()


imageSize = img_file2.shape     # получение размерности в виде: [x, y, z], где z=4 это кол-во сторон что ли, я не понял
# далее запись в матрицу кортежей значений с цветами пикселей
pixels_list = []
for i in range(imageSize[0]):
    pixels_list.append([])
    for j in range(imageSize[1]):
        pixels_list[i].append(tuple(img_file2[j][i]))

# преобразование квадрата пикселей(16 на 16 в момент написания), в пиксели одного яркого цвета, цвет должен браться из базы данных цветов colors.py
pixels_list_edit = pixels_list
try:
    for i in range(0, imageSize[0], 4):
        for j in range(0, imageSize[1], 4):
            temp = []   #промежуточные пиксели
            for m in range(4):
                temp.append(pixels_list[i+m][j])
                temp.append(pixels_list[i+m][j+1])
                temp.append(pixels_list[i+m][j+2])
                temp.append(pixels_list[i+m][j+3])
            pixels = []
            for k in range(4):
                sumTemp = 0
                for l in range(16):      # кол-во пикселей всего
                    sumTemp += temp[l][k]
                pixels.append(sumTemp//4)
            pixels_list_edit[i][j] = pixels_list_edit[i][j+1] = pixels_list_edit[i+1][j] = pixels_list_edit[i+1][j+1] = tuple(pixels)

except:
    print('pixel broken')



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
