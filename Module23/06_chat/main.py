while True:
    action = input('\nФункции: Посмотреть текущий текст чата - 1 | Отправить сообщение  - 2\n')
    if action == '1':
        with open('chat.txt', 'r', encoding='utf-8') as chat_r:
            print('\n', chat_r.read())
    elif action == '2':
        message = input('\nВведите сообщение:\n')
        with open('chat.txt', 'a', encoding='utf-8') as chat_w:
            chat_w.write(message + '\n')
    else:
        print('Ошибка ввода!')
