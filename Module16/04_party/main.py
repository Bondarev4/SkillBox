guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    n = len(guests)
    print('Сейчас на вечеринке', n, 'человек:', guests)
    action = input('Гость пришел или ушел? ')
    if action == 'пришел':
        name = input('Имя гостя: ')
        if n > 5:
            print('Прости, ' + name + ', но мест нет.')
        else:
            guests.append(name)
            print('Привет, ' + name + '!')
    elif action == 'ушел':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока, ' + name + '!')
    else:
        print('Вечеринка закончилась, все легли спать.\n...')
        break

