s = 0
with open('calc.txt', 'r') as file:
    for line in file:
        data = line.split()
        signs = ['+', '-', '*', '/', '%', '^']
        sign = data[1]
        if len(data) == 3 and data[0].isdigit() and data[2].isdigit() and sign in signs:
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
