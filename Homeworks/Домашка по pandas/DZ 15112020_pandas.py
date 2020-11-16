##Задание 1
##Скачайте с сайта https://grouplens.org/datasets/movielens/
##датасет любого размера. Определите какому фильму
##было выставлено больше всего оценок 5.0.

import pandas as pd

movies=pd.read_csv('movies.csv')
movies[['movieId','title']].head()

ratings=pd.read_csv('ratings.csv')
ratings=ratings[['movieId','rating']]

joined = ratings.merge(movies, on='movieId', how='left')
joined[['movieId','rating','title']].head()

max_=ratings['rating'].max()
filtered_joined=joined[(joined ['rating']==max_)]
fr=filtered_joined.groupby(['movieId' , 'title'])['movieId'].count()

print(fr.sort_values(ascending=False).head())


##Задание 2
##По данным файла power.csv посчитайте суммарное потребление стран Прибалтики
##(Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года.
##Не учитывайте в расчетах отрицательные значения quantity.

import pandas as pd

power=pd.read_csv('power.csv')
power.head()

filtered_countries = power[(power['country']=='Estonia') | (power['country']=='Lithuania') | (power['country']=='Latvia') ]
filtered_countries.head()

fc=filtered_countries[(filtered_countries['category']==4) | (filtered_countries['category']==12) | (filtered_countries['category']==21) & (filtered_countries['year']<2010) & (filtered_countries['year']>2005)]

print('Количество потребления для стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года равно {}КВт'.format(fc['quantity'].sum()))

##Задание 3
##Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.

import pandas as pd

data=pd.read_html('https://www.finanz.ru/valyuty/v-realnom-vremeni')[1]
print(data.head())


