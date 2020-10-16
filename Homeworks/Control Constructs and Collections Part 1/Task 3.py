#Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
#Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
#Но мы не будем никого знакомить, если кто-то может остаться без пары:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()


if len(boys) == len(girls):
    print('Идеальные пары:')
    for x in range(len(girls)):
        print(boys[x], 'и', girls[x])
else:
    print('Внимание, кто-то может остаться без пары!')


