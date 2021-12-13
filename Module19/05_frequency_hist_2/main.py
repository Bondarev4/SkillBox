string = input('Введите текст: ')
counter_alpha = {}
been = []
for letter in string:
    if letter not in been:
        k = string.count(letter)
        if k not in counter_alpha:
            counter_alpha[k] = [letter]
        else:
            counter_alpha[k].append(letter)
        been.append(letter)
print('Инвертированный словарь частот:')
for key in counter_alpha.keys():
    print(key, ':', counter_alpha[key])