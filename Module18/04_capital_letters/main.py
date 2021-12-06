string = input('Введите строку: ').split()
print('\nРезультат:', end=' ')
for word in string:
    print(word.capitalize(), end=' ')