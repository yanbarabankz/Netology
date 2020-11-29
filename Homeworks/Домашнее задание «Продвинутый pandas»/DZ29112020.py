##Задание 1
##Для датафрейма log из материалов занятия создайте столбец source_type по следующим правилам:
##
##если источник traffic_source равен yandex или google, то в source_type ставится organic
##для источников paid и email из России - ставим ad
##для источников paid и email не из России - ставим other
##все остальные варианты берем из traffic_source без изменений



import pandas as pd

log=pd.read_csv('visit_log.csv', sep=';')

def filtered(row):
    if row['traffic_source']=='yandex':
        return 'organic'
    elif row['traffic_source']=='google':
        return 'organic'
    elif row['traffic_source']=='paid':
        if row['region']=='Russia':
            return 'ad'
        else:
            return 'other'
    elif row['traffic_source']=='email':
        if row['region']=='Russia':
            return 'ad'
        else:
            return 'other'
    else:
        return row['traffic_source']

log['source_type']=log.apply(filtered, axis=1)

print(log.head(10))

##Задание 2
##В файле URLs.txt содержатся url страниц новостного сайта. Вам необходимо отфильтровать его по адресам страниц с текстами новостей. И
##звестно, что шаблон страницы новостей имеет внутри url следующую конструкцию: /, затем 8 цифр, затем дефис. Выполните следующие действия:
##
##Прочитайте содержимое файла с датафрейм
##Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствии с заданным шаблоном

import pandas as pd
import re

urls=pd.read_csv('URLs.txt')
print(urls[urls.url.str.contains('/[0-9]{8}-', regex=True)].head())

##Домашнее задание 3
##В датафрейме data создайте столбец lemmas, в котором вычислите леммы поисковых запросов из столбца keyword. Леммы должны иметь строковый тип.

import pandas as pd
from pymystem3 import Mystem

data = pd.DataFrame({
    'keyword': ['курс гривны к рублю', 'доллары в рубли', '100 долларов в рублях', 'курс рубля'],
    'shows': [125076, 114173, 97534, 53546],
})

def lemmas_function(row):
    m=Mystem()
    lemma = m.lemmatize(row['keyword'])
    string = ' '.join(lemma)
    return string


data['lemmas']=data.apply(lemmas_function, axis=1)

print(data)

