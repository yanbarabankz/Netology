##Задание 1
##
##Используйте файл с оценками фильмов ml-latest-small/ratings.csv.
##Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок.
##Под временем жизни понимается разница между максимальным и минимальным значением столбца timestamp для данного значения userId.

import pandas as pd

ratings=pd.read_csv('ratings.csv', sep=',')

ratings_count=ratings.groupby('userId').count().reset_index()
ratings_count=ratings_count[['userId','rating']]

count_more_than_100=ratings_count[ratings_count['rating']>100]
count_more_than_100.rename(columns={'rating': 'rating_count'}, inplace=True)

rating_max=ratings.groupby('userId').max().reset_index()
rating_min=ratings.groupby('userId').min().reset_index()

rating_max_timestamp=rating_max[['userId','timestamp']]
rating_min_timestamp=rating_min[['userId','timestamp']]

rating_max_timestamp.rename(columns={'timestamp': 'timestamp_max'}, inplace=True)
rating_min_timestamp.rename(columns={'timestamp': 'timestamp_min'}, inplace=True)

avg_timestamp=count_more_than_100.merge(rating_max_timestamp, how='inner').merge(rating_min_timestamp, how='inner')

def average(row):
    mean_=(row['timestamp_max']-row['timestamp_min'])
    return mean_

avg_timestamp['avg']=avg_timestamp.apply(average, axis=1)
len(count_more_than_100)==len(avg_timestamp)

print(avg_timestamp.head(10))

##Задание 2
##
##Дана статистика услуг перевозок клиентов компании по типам (см. файл с кодом занятия). Необходимо сформировать две таблицы:
##таблицу с тремя типами выручки для каждого client_id без указания адреса клиента
##аналогичную таблицу по типам выручки с указанием адреса клиента
##Обратите внимание, что в процессе объединения таблиц данные не должны теряться.

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1', 
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

table=rzd.merge(auto, how='outer', on='client_id')
table=table.merge(air, how='outer', on='client_id')
table.loc[table.rzd_revenue.isnull(), 'rzd_revenue',]=0
table.loc[table.auto_revenue.isnull(), 'auto_revenue',]=0
table.loc[table.air_revenue.isnull(), 'air_revenue',]=0
full_table=table.merge(client_base, how='outer', on='client_id')

print(full_table)


##Задание 3
##
##В задаче сквозной аналитики вам предоставили данные по местоположению пользователей.
##Т. е. для каждого user_id известна последовательность координат (широта/долгота), когда они требовались приложению для полноценной работы. Как бы вы добавили эти сведения в таблицу визитов и покупок? Для составления ответа можно использовать вопросы:
##У каждого пользователя известен набор координат. А для связывания с визитом или фактом покупки скорее всего потребуется одно-два числа. Как их получить?
##Наборы координат одного и того же пользователя могут быть значительно удалены друг от друга. Как это отразится на вопросе расчетах пункта 1?
##Какие дополнительные признаки можно получить из координат? Ведь это просто числа, которые сами по себе мало что дают.
##

coordinates = pd.DataFrame(
    {
        'user_id': [11, 22, 55, 11, 99],
        'visit_id': [101, 301, 305, 896, 896],
        'coordinate': ['55.755831 37.617673', '56.755831 37.617673', '55.755831 38.617673', '55.755831 37.617673', '55.255831 37.017673'],
    }
)

print(coordinates)

