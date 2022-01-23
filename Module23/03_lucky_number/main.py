import random


def random_delete(text):
    unlucky_line = random.randint(0, text.read().count('\n'))
    lines_list = text.readlines()
    lines_list[unlucky_line] = '\n'
    text.writelines(lines_list)


s = 0
with open('lucky_number.txt', 'w') as file:
    while s < 777:
        try:
            if random.randint(1, 13) == 13:
                random_delete(file)
                raise TypeError
            number = int(input('Введите число: '))
            s += number
            file.write(str(number) + '\n')
        except TypeError:
            print('Вас постигла неудача!')
with open('lucky_number.txt', 'r') as file_2:
    print('\nСодержимое файла out_file.txt:')
    print(file_2.read())
