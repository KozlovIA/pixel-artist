# Ковертирование изображения в пиксельное
# Изображение и изображение Чтение изображений
from PIL import Image
from skimage import io
import time

start_time = time.time()

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
n=2     # корень из кол-ва пикселей
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


# Преобразование средних значений к ближайшему цвету, где r, g и b кратно 63 (63*r, 63*g, 63*b)
for i in range(imageSize[0]):
    for j in range(imageSize[1]):
        current_pixel = pixels_list_edit[i][j]  # текущий пиксель изображения в формате RGB
        red = round(current_pixel[0]/63, 0)*63
        green = round(current_pixel[1]/63, 0)*63
        blue = round(current_pixel[2]/63, 0)*63
        pixels_list_edit[i][j] = (int(red), int(green), int(blue))
        


# преобразование из матрицы в список, для использования в функции putdata()
new_list = []
for i in range(0, imageSize[0]):
    for j in range(0, imageSize[1]):
        new_list.append(pixels_list_edit[i][j])


im = Image.new('RGB', (imageSize[0], imageSize[1]))
im.putdata(new_list)
im_rotate = im.rotate(-90)
im_flip = im_rotate.transpose(Image.FLIP_LEFT_RIGHT)
im_flip.save('result.png')


print("Программа завершена, с запуска прошло", round(time.time() - start_time, 2), "сек")