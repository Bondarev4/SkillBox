import os


def file_txt(my_text):
    path = ' ' + input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n')
    path = path.replace(' ', '\\')
    name = input('\nВведите имя файла: ')
    path = os.path.join(path, name + '.txt')
    if os.path.exists(path):
        flag = input('Вы действительно хотите перезаписать файл? ').lower()
        if flag == 'да':
            f = open(path, 'w')
            f.write(my_text)
            print('Файл успешно перезаписан!')
            f.close()
        else:
            print('Файл не изменен!')
    else:
        f = open(path, 'w')
        f.write(my_text)
        print('Файл успешно перезаписан!')
        f.close()


text = input('Введите строку: ')
file_txt(text)