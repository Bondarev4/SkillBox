string = input('Введите строку: ')
f_h = string.index('h')
string = string[::-1]
print(string[string.index('h') + 1:(f_h * (-1) - 1)])
