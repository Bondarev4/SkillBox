s = 0
with open('calc.txt', 'r') as file:
    for line in file:
        data = line.split()
        signs = ['+', '-', '*', '/', '%', '^']
        sign = data[1]
        try:
            if len(data) != 3 or not data[0].isdigit() or not data[2].isdigit() or not sign in signs:
                raise ValueError
        except ValueError:
            fix = input('Обнаружена ошибка в строке: {}\tХотите исправить? '.format(line))
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
