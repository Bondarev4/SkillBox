import os.path

def m_l(text):
    letters_list = list()
    al = ''
    min_c = 0
    for sym in text:
        if sym.isalpha():
            sym = sym.lower()
            if sym not in letters_list:
                c_s = text.count(sym)
                if c_s < min_c or min_c == 0:
                    al = sym
                    min_c = c_s
                letters_list.append(sym)
    return al


way = os.path.abspath(os.path.join('../../', 'Module22', '02_zen_of_python', 'zen.txt'))
file = open(way, 'r')
strings = 0
words = -1
letters = 0
for string in file:
    strings += 1
    words += len(string.split())
    for letter in string.lower():
        if letter.isalpha():
            letters += 1
print('Количество букв в файле:', letters)
print('Количество слов в файле:', words)
print('Количество строк в файле:', strings)
print('Наиболее редкая буква:', m_l(open(way, 'r').read()))
file.close()