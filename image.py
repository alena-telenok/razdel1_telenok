import os

import cv2
import random

#image = cv2.imread('smeshariki.jpg')

# ВНИМАНИЕ! В OpenCV первым аргументом идет ВЫСОТА!
# sliced_region = image_np[:, 50:150]

#print(f'image shape = {image.shape}')

#height = image.shape[0]
#width = image.shape[1]
#depth = image.shape[2]

# ВНИМАНИЕ! В OpenCV первым аргументом идет ВЫСОТА!
# image[height // 2:height , 50:150] = [0, 0, 255]
# image[:height // 2, 150:200] = [255, 0, 0]

while True:
    name = input("Введите имя изображения, которое хотите загрузить")
    image = cv2.imread(name)
    if None is image:
        print("Пожалуйста введите правильное имя")
    elif None is not image:
        break

height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]
print(f'Параметры картинки: высота - {height}, ширина - {width}, глубина - {depth}, тип - {image.dtype}')


while True:
    operation = input("Выберите, что сделать с картинкой: применить эффект (1) или сохранить (2)?")
    if '1' == operation:
        effect = input("Выберите эффект: сделать изображение черно-белым (1), отразить изображение по вертикальной оси (2), отразить изображение по горизонтальной оси (3), закрасить случайный квадрат изображения в выбранный цвет (4), добавить шум к изображению (5), увеличить/уменьшить яркость изображения (6), размыть изображение(7), увеличить/уменьшить контрастность изображения (8)?")
        if '1' == effect:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        if '2' == effect:
            roi = image[:, :width // 2]
            image[:, width // 2:] = cv2.flip(roi, 1)
        if '3' == effect:
            roi = image[:height // 2, :]
            image[height // 2:, :] = cv2.flip(roi, 0)
        if '4' == effect:
            y = random.randint(0, height - 100)
            x = random.randint(0, width - 100)
            color = input("Введите цвет, в который хотите закрасить квадрат: синий (1), заленый (2), красный (3)")
            if '1' == color:
                color = [255,0,0]
            elif '2' == color:
                color = [0,255,0]
            elif '3' == color:
                color = [0,0,255]
            image[y:y + 100, x:x + 100] = color
        if '5' == effect:
            tenpercent = round(height * width // 10)
            pixels = [dict({ 'y': random.randint(0, height - 1), 'x': random.randint(0, width - 1) }) for let in range(0, tenpercent)]
            for pixel in pixels:
                image[pixel.get('y'), pixel.get('x')] = image[random.randint(0, height - 1), random.randint(0, width - 1)]
        if '6' == effect:
            bright = input("Введите, как вы хотите изменить яркость: увеличить (1) или уменьшить (2)?")
            if '1' == bright:
                image = cv2.convertScaleAbs(image,  alpha=1, beta=50)
            elif '2' == bright:
                image = cv2.convertScaleAbs(image, alpha=1, beta=-50)
        if '7' == effect:
            image = cv2.blur(image, (10, 10))
        if '8' == effect:
            kontrast = input("Введите, как вы хотите изменить контрастность: увеличить (1) или уменьшить (2)?")
            if '1' == kontrast:
                image = cv2.convertScaleAbs(image,  alpha=1.5, beta=0)
            elif '2' == kontrast:
                image = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
    elif '2' == operation:
        while True:
            try:
                name = input("Введите имя изображения, которое хотите сохранить")
                cv2.imwrite(name, image)
                print(os.path.abspath(name))
                break
            except Exception as error:
                print(f'Пожалуйста введите правильное имя ({type(error)}): {error}')
        break

#roi = image[:height // 2, :]

#roi[:,:, 0] = 0
#roi[:,:, 1] = 0

#image[height // 2:, :] = roi

# cv2.imshow('Sliced Image', sliced_region)
cv2.imshow('Sliced Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()