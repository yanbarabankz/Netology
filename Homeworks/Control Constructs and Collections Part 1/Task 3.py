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



