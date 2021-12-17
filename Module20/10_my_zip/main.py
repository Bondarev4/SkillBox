string = input('Строка: ')
trp = (int(x) for x in input('Кортеж чисел: ').split())
s_l = len(string)
analogue_zip = ((string[i], el) for i, el in enumerate(trp) if i < s_l)
print('\nРезультат:', analogue_zip)
for x in analogue_zip:
    print(x)