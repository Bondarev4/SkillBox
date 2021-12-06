ip = input('Введите IP: ').split('.')
flag = True
for el in ip:
    if el.isalnum():
        print('Адрес - это четыре числа, разделенные точками')
        flag = False
        break
    if not el.isdigit():
        print(el, 'не целое число')
        flag = False
        break
    elif int(el) > 255:
        print(el, 'превышает 255')
        flag = False
        break
if flag:
    print('IP-адрес корректен')