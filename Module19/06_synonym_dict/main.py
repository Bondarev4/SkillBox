n = int(input('Введите количество пар слов: '))
synonyms = {}
for i in range(1, n + 1):
    pair = input(str(i) + ' пара: ').lower().split(' - ')
    synonyms[pair[0]] = pair[1]
    synonyms[pair[1]] = pair[0]
print()
while True:
    word = input('Введите слово: ').lower()
    if word in synonyms:
        print('Синоним:', synonyms[word].capitalize())
    else:
        print('Такого слова в словаре нет.')
