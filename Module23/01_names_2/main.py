def len_line(line_text, i_l):
    c = len(line_text) - 1
    return c


i_line = 0
count_symbols = 0
with open('people.txt', 'r') as people_file:
    for line in people_file:
        i_line += 1
        symbols_in_line = len_line(line, i_line)
        try:
            if symbols_in_line < 3:
                raise TypeError
            count_symbols += symbols_in_line
        except TypeError:
            print('В {} строке меньше 3 символов'.format(i_line))
print(count_symbols)