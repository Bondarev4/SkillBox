string = input('Введите текст: ')
vowel_rus = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowel_text = [letter for letter in string if letter in vowel_rus]
print('\nСписок гласных букв:', vowel_text)
print('Длина списка:', len(vowel_text))
