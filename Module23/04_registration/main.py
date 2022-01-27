def type_error(data_line):
    data = data_line.split()
    try:
        if len(data) < 3:
            raise IndexError
        elif not data[0].isalpha():
            raise NameError
        elif not data[1].count('@') or not data[1].count('.'):
            raise SyntaxError
        elif not data[2].isdigit() or not 9 < int(data[2]) < 100:
            raise ValueError
    except IndexError:
        return 'НЕ присутствуют все три поля'
    except NameError:
        return 'поле имени содержит НЕ только буквы'
    except SyntaxError:
        return 'поле емейл НЕ содержит @ и .(точку)'
    except ValueError:
        return 'поле возраст НЕ является числом от 10 до 99'
    return 0


good = open('registrations_good.log', 'w')
bad = open('registrations_bad.log', 'w')

with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        error = type_error(line)
        if error:
            bad.write('\t\t'.join([line[:-1], error, '\n']))
        else:
            good.write(line)

good.close()
bad.close()
