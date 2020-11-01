#Задание 1
#Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
#The Moscow Times - Wednesday, October 2, 2002
#The Guardian - Friday, 11.10.13
#Daily News - Thursday, 18 August 1977

from datetime import datetime

date_string = 'Wednesday, October 2, 2002'
date_datetime = datetime.strptime(date_string, '%A, %B %d, %Y')
print(date_datetime)

date_string = 'Friday, 11.10.13'
date_datetime = datetime.strptime(date_string, '%A, %d.%m.%y')
print(date_datetime)

date_string = 'Thursday, 18 August 1977'
date_datetime = datetime.strptime(date_string, '%A, %d %B %Y')
print(date_datetime)





#Задание 2
#Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
#stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]

#Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

from datetime import datetime

stream = [
    '2018-04-02', 
    '2018-02-29', 
    '2018-19-02']
def check_date(list_date):
    for date in list_date:
        try:
            valid_date = datetime.strptime(date, '%Y-%m-%d')
            print(True)    
        except ValueError:
            print(False)
check_date(stream)

#Задание 3
#Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. Даты должны вводиться в формате YYYY-MM-DD.
#В случае неверного формата или при start_date > end_date должен возвращаться пустой список.


from datetime import timedelta
from datetime import datetime
start_date=input('Введите начальную дату в формате YYYY-MM-DD: ')
end_date=input('Введите дату окончания в формате YYYY-MM-DD: ')
def date_range(start, end):
    start_datetime=datetime.strptime(start,'%Y-%m-%d')
    end_datetime=datetime.strptime(end,'%Y-%m-%d')
    days=[]
    if start_datetime<end_datetime:
        intermediate_datetime=start_datetime
        while intermediate_datetime<=end_datetime:
            intermediate_datetime=intermediate_datetime+timedelta(days=1)
            print_datetime=datetime.strftime(intermediate_datetime,'%Y-%m-%d')
            days.append(print_datetime)
            print(print_datetime)
    return(days)
date_range(start_date, end_date)



