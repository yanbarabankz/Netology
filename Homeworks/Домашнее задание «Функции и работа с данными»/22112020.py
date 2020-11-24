##Задание 1**
##Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
##- оценка 2 и меньше - низкий рейтинг
##- оценка 4 и меньше - средний рейтинг
##- оценка 4.5 и 5 - высокий рейтинг
##
##Результат классификации запишите в столбец class


import pandas as pd

raiting=pd.read_csv('ratings.csv')

def class_movies(row):
    if row['rating']<=2.0:
        return 'низкий рейтинг'
    elif 2.0<row['rating']<=4.0:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'

raiting['class'] = raiting.apply(class_movies, axis=1)
print(raiting.head())

##Задание 2
##Используем файл keywords.csv.
##
##Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определенному региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
##
##Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:
##
##geo_data = {
##
##'Центр': ['москва', 'тула', 'ярославль'],
##
##'Северо-Запад': ['петербург', 'псков', 'мурманск'],
##
##'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
##}
##
##Результат классификации запишите в отдельный столбец region.

geo_data = {

'Центр':['москва', 'тула', 'ярославль'],

'Северо-Запад':['петербург', 'псков', 'мурманск'],

'Дальний Восток':['владивосток', 'сахалин', 'хабаровск'] 
}

towns=[]
for values in geo_data.values():
    for i in values:
        towns.append(i)

row='вконтакте моя страница москва'
data=row.split(' ')
def check(t):
    for i in t:
        if i in towns:
            for items in geo_data.items():
                if i in items[1]:
                    print(items[0])

df=pd.read_csv('keywords.csv')

def region_in_keyword(row):
    data=row['keyword'].split(' ')
    i=0
    for word in data:
        if word in towns:
            for items in geo_data.items():
                if word in items[1]:
                    i+=1
                    return items[0]
    if i==0:
        return 'undefined'

df['region'] = df.apply(region_in_keyword, axis=1)


print(df[(df['region']!='undefined')])


