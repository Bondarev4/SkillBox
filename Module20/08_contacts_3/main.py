phone_numbers = dict()

while True:
    action = int(input('\n'.join(['\nВведите номер действия:', ' 1. Добавить контакт', ' 2. Найти человека\n'])))
    if action == 1:
        name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if name in phone_numbers:
            print('Такой человек уже есть в контактах.')
        else:
            number = input('Введите номер телефона: ')
            phone_numbers[name] = number
        print('Текущий словарь контактов:', phone_numbers)
    elif action == 2:
        surname_search = input('Введите фамилию для поиска: ')
        for name, surname in phone_numbers.keys():
            if surname == surname_search:
                print(name, surname, phone_numbers[name, surname])
    else:
        print('Ошибка --> Такой команды не существует')
