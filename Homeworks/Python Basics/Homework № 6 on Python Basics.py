import math
num = input("Площадь какой фигуры необходимо вычислить: ")

if num == "Круг":
    radius = int(input('Укажите радиус круга: '))
    square = round(radius * radius * math.pi, 1)
    print('Площадь круга: ', square)
if num == 'Треугольник':
    a = int(input('Введите длину стороны А: '))
    b = int(input('Введите длину стороны B: '))
    c = int(input('Введите длину стороны C: '))
    p = (a+b+c)/2
    square = round((p*(p-a)*(p-b)*(p-c))**0.5, 1)
    print('Площадь треугольника равна', square)
if num == 'Прямоугольник':
    a = int(input('Введите длину стороны А: '))
    b = int(input('Введите длину стороны B: '))
    square = round(a*b, 1)
    print('Площадь прямоугольника равна', square)
    print()


