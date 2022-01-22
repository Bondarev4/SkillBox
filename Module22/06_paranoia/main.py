def caeser_text(text):
    l_l = 'abcdefghijklmnopqrstuvwxyz'
    h_l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = open('cipher_text.txt', 'w')
    for i, ln in enumerate(text):
        for letter in ln:
            if letter.islower():
                new.write(l_l[(l_l.index(letter) + i + 1) % 27])
            elif letter.isupper():
                new.write(h_l[(h_l.index(letter) + i + 1) % 27])
            else:
                new.write(letter)
    new.close()


file = open('text.txt', 'r')
print('Содержимое файла text.txt:')
print(file.read())
file = open('text.txt', 'r')
caeser_text(file)
n_f = open('cipher_text.txt', 'r')
print('\nСодержимое файла cipher_text.txt:')
print(n_f.read())
file.close()
n_f.close()