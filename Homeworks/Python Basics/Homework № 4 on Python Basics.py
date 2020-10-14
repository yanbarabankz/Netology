while True:
    width = int(input('Ширина, см: '))
    length = int(input('Длина, см: '))
    height = int(input('Высота, см: '))
    if length > 200:
        print('Упаковка для лыж')
    elif width < 15 and length < 15 and height < 15:
        print ("Коробка № 1")
    elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
        print('Коробка № 2')
    else:
        print('Стандартная коробка №3')
    print()
