documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def people(numbers):
    for doc_numbers in documents:
        if doc_numbers["number"] == numbers:
            print(doc_numbers["name"])
            break
    else:
        print('Документ не найден в базе.')

def shelf(numbers):
    break_marker = False
    for shelf_directories in directories.items():
        for doc_numbers in shelf_directories[1]:
            if doc_numbers == numbers:
                print('Документ хранится на полке:', shelf_directories[0])
                break_marker = True
                break
        if break_marker == True:
            break
    else:
        print('Документ не найден в базе.')

def people_list():
    for persons in documents:
        print('№:' +  persons['number'] + ', тип:' + persons['type'] + ', владелец:' + persons['name'])

def add(number):
    directories[number] = 10
    print('Полка добавлена. Текущий перечень полок:', *directories.keys(), sep=",")

def delete(number):
    if len(directories.get(number)) != 0:
        print('На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:', *directories.keys(), sep=", ")
    elif number in directories:
        directories.pop(number, None)
        print('Полка удалена. Текущий перечень полок:', *directories.keys(), sep=", ")
    else:
        print('Такой полки не существует. Текущий перечень полок:', *directories.keys(), sep=", ")

while True:
    command = input('\n \
  Введите одну из команд: p, l, s, ds, as. \n \
  Для выхода наберите exit. \n \
  Для вызов справки наберите help. \n \
  Ваша команда: ')
    if command == 'p':
        people(input('\nВведите номер документа:'))
    elif command == 's':
        shelf(input('\nВведите номер документа:'))
    elif command == 'l':
        people_list()
    elif command == 'as':
        add(input('Введите номер полки:'))
    elif command == 'ds':
        delete(input('Введите номер полки:'))
    elif command == 'exit':
        break
    elif command == 'help':
        print('\n \
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n \
    l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n \
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n \
    as – add – команда, которая добавит новую полку')
    else:
        print('Вы ввели некорректную команду, повторите ввод.')

