import random


s = 0
try:
    with open('lucky_number.txt', 'w+') as file:
        while s < 777:
            if random.randint(1, 13) == 13:
                raise TypeError
            number = int(input('Введите число: '))
            s += number
            file.write(str(number) + '\n')

except TypeError:
    print('Вас постигла неудача!')
    file_1 = open('lucky_number.txt', 'r+')
    count_lines = file_1.read().count('\n')
    if count_lines != 0:
        unlucky_line = random.randint(0, count_lines - 1)
        file_2 = open('lucky_number.txt', 'r')
        lines_list = file_2.readlines()
        lines_list[unlucky_line] = '\n'
        file_3 = open('lucky_number.txt', 'w')
        file_3.writelines(lines_list)
        file_2.close()
        file_3.close()
    file_1.close()

finally:
    with open('lucky_number.txt', 'r') as file_4:
        print('\nСодержимое файла out_file.txt:')
        print(file_4.read())
