message = input('Сообщение: ')
new_message = ''
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
word = ''
for letter in message:
    if letter not in punctuation:
       word = letter + word
    else:
        new_message += word
        new_message += letter
        word = ''
print('\nНовое сообщение:', new_message)