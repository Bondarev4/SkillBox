string1 = input('Первая строка: ')
string2 = input('Вторая строка: ')
flag = False
count = 0
n1 = len(string1)
n2 = len(string2)
if string1 == string2:
    flag = True
elif n2 == n1:
    while not flag and count < n1 - 1:
        string1 = string1[-1] + string1[0:-1]
        count += 1
        if string1 == string2:
            flag = True
if flag:
    print('Первая строка получается из второй со сдвигом ' + str(count) + '.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
