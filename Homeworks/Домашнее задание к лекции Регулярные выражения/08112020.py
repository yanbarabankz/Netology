#Задание 1

#Напишите функцию, которая принимает на вход строку
#и проверяет является ли она валидным транспортным номером
#(1 буква, 3 цифры, 2 буквы, 2-3 цифры).
#Обратите внимание, что не все буквы кириллического алфавита
#используются в транспортных номерах.

#Если номер валиден, то функция должна возвращать отдельно номер и регион.


import re

number_car=input('Введите гос номер: ')
def print_num_reg(number):
    regex_number='^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}'
    if re.match(regex_number, number):
        print('Номер {} правильный'.format(number))
        regex=r'\d+'
        number_and_region=re.findall(regex, number)
        print(number_and_region)
    else:
        print ('Номер неверный!')
print_num_reg(number_car)

#Задание 2

#Напишите функцию, которая будет удалять все последовательные
#повторы слов из заданной строки при помощи регулярных выражений.


def regex_replay(string):
    regex=r'(.+?)\1+'
    result=re.sub(regex, r'\1',string)
    print(result)
regex_replay('too be be the was were were be be be')

#Задание 3

#Напишите функцию, которая будет возвращать акроним
#по переданной в нее строке со словами.


print_str=input()
def print_acronym(string):
    regex=r'(\b\w)'
    list_find=re.findall(regex, string)
    str_find=''.join(list_find)
    print(str_find)
print_acronym(print_str)


#Задание 4

#Напишите функцию, которая будет принимать на вход список email-адресов
#и выводить их распределение по доменным зонам.
#Пример работы программы:
#emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']
#Результат:
#gmail.com: 2
#test.in: 1 
#ya.ru: 2 
#mail.ru: 1

import re

result = re.findall(r'@\w+.\w+', 'test@gmail.com, xyz@test.in, test@ya.ru, xyz@mail.ru, xyz@ya.ru, xyz@gmail.com')
total = dict((i, result.count(i)) for i in result)

for key in total:
    print(key, ':', total[key])








