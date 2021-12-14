string = input('Введите строку: ')
letters = set(string)
flag = True
if len(string) % 2 == 0:
    for el in string:
        if string.count(el) % 2 != 0:
            flag = False
            break
else:
    flag_odd = False
    for el in string:
        if string.count(el) % 2 == 1:
            if flag_odd:
                flag = False
                break
            flag_odd = True
if flag:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')