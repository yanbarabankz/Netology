#Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. 
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100
#Пример работы программы:

results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}

for key, value in results.items():
    results[key]['ROI'] = round(((value['revenue']/value['cost']-1)*100), 2)


print('Результат:', results)




