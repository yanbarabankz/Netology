#Задание 1
#Напишите функцию, которая возвращает название валюты (поле ‘Name’)
#с максимальным значением курса с помощью сервиса
#https://www.cbr-xml-daily.ru/daily_json.js

import requests

class Rate:
    def __init__(self, format_='value'):
        self.format = format_
    
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
       
    def max_cource(self):
        response = self.exchange_rates()
        max_course=0
        for row in response.values():
            value=row['Value']
            if max_course<=value:
                max_course=value
                name=row['Name']
        print(row['Name'], max_course)

Rate().max_cource()

#Задание 2
#Добавьте в класс Rate параметр diff (со значениями True или False),
#который в случае значения True в методах курсов валют (eur, usd итд)
#будет возвращать не курс валюты, а изменение по сравнению в прошлым
#значением. Считайте, self.diff будет принимать значение True
#только при возврате значения курса.
#При отображении всей информации о валюте он не используется.

import requests

class Rate:
    def __init__(self, format_='value', check='True'):
        self.format = format_
        self.check = check
    
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def diff(self, check):
        self.check=check
    
    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                if self.check=='True':
                    difference=response[currency]['Previous']-response[currency]['Value']
                    return difference
                else:    
                    return response[currency]['Value']
        
            return 'Error'
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')
    


print(Rate('value', 'False').usd())


#Задание 3

#Напишите класс Designer, который учитывает количество международных премий
#для дизайнеров (из презентации: “Повышение на 1 грейд за каждые 7 баллов.
#Получение международной премии – это +2 балла”).
#Считайте, что при выходе на работу сотрудник уже имеет две премии
#и их количество не меняется со стажем
#(конечно если хотите это можно вручную менять).

class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards= awards
        self.grade = 1
    
    def grade_up(self):
        self.grade += 1
    
    def publish_grade(self):
        print(self.name, self.grade)
        
class Developer(Employee):
    def __init__(self, name, seniority, awards=0):
        super().__init__(name, seniority, awards=0)
    
    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1
        if self.seniority % 5 == 0:
            self.grade_up()
        return self.publish_grade()

class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)
        
    def check_if_it_is_time_for_upgrade(self):
        if self.seniority==0: 
            self.seniority=1+self.awards*2
        else:
            self.seniority+=1
        if self.seniority % 7==0:
                self.grade_up()
        
        return self.publish_grade()

elena = Designer('Елена', seniority=0, awards=2)

for i in range(20):
    elena.check_if_it_is_time_for_upgrade()

