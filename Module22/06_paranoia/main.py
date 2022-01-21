import os

l_l = 'abcdefghijklmnopqrstuvwxyz'
h_l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caeser_text(text):



file = open('text.txt', 'r')
print('Содержимое файла text.txt:')
for line in file:
    print(line)
caeser_text(file.read())
print('Содержимое файла cipher_text.txt:')
file.close()