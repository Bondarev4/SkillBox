def unique_letter(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count == 1


w = input('Введите слово: ')
counter = 0
for l in w:
    if unique_letter(w, l):
        counter += 1
print('\nКол-во уникальных букв:', counter)