import random


s = 0
try:
    with open('lucky_number.txt', 'w+') as file:
        while s < 777:
            if random.randint(1, 6) == 4:
                raise TypeError
            number = int(input('Введите число: '))
            s += number
            file.write(str(number) + '\n')

except TypeError:
    print('Вас постигла неудача!')
    with open('lucky_number.txt', 'r+') as file_1:
        print('----------')
        count_lines = file_1.read().count('\n')
        if count_lines != 0:
            unlucky_line = random.randint(0, count_lines - 1)

            lines_list = file_1.readlines()
            print(lines_list)
            # lines_list[] = '\n'
            print(lines_list)
            print('----------')
            # file.writelines(lines_list)

finally:
    with open('lucky_number.txt', 'r') as file_2:
        print('\nСодержимое файла out_file.txt:')
        print(file_2.read())
