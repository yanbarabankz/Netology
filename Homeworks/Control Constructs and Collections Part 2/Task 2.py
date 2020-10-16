
#Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже).
#Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

two_words = 0
three_words = 0

for x in range(len(queries)):
    if len(queries[x].split(' ')) == 2:
        two_words += 1
    else:
        three_words += 1

two_words_percent = round((two_words*100)/(two_words+three_words), 2)
three_words_percent = round((three_words*100)/(two_words+three_words), 2)

print('Поисковых запросов, содержащих 2 слов(а): ', two_words_percent, '%')
print('Поисковых запросов, содержащих 3 слов(а): ', three_words_percent, '%')
