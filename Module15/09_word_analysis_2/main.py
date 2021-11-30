word = input('Введите слово: ')
flag = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        flag = False
        break
if flag:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
