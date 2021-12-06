string = input('Введите строку: ')
el = [string[0]]
last = string[0]
count = 0
for letter in string:
    if letter == last:
        count += 1
    else:
        el.append(str(count))
        el.append(letter)
        last = letter
        count = 1
el.append(str(count))
print('\nЗакодированная строка:', ''.join(el))