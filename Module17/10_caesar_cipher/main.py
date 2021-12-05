string = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
code = [alphabet[(alphabet.index(letter) + k) % 33] if letter != ' ' else ' ' for letter in string]
print('Зашифрованное сообщение:', end=' ')
for x in code:
    print(x, end='')
