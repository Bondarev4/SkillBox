s = 0
with open('calc.txt', 'r') as file:
    for line in file:
        data = line.split()
        signs = ['+', '-', '*', '/', '%', '^']
        sign = data[1]
        try:
            if len(data) != 3 or not data[0].isdigit() or not data[2].isdigit() or sign not in signs:
                raise ValueError
        except ValueError:
            fix_flag = input('Обнаружена ошибка в строке: {}\tХотите исправить? '.format(line)).lower()
            if fix_flag == 'нет':
                continue
            else:
                fix = input('Введите исправленную строку: ')
                with open('calc.txt', 'r') as file_a:
                    lines_list = file_a.readlines()
                    lines_list[lines_list.index(line)] = fix + '\n'
                with open('calc.txt', 'w') as file_b:
                    file_b.writelines(lines_list)
                data = fix.split()
                sign = data[1]
        a, b = int(data[0]), int(data[2])
        if sign == '+':
            s += a + b
        elif sign == '-':
            s += a - b
        elif sign == '*':
            s += a * b
        elif sign == '/':
            s += a // b
        elif sign == '%':
            s += a % b
        else:
            s += a ^ b
print(s)
