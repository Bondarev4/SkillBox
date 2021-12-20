def find_key(struct, k, depth):
    if k in struct:
        return struct[k]
    if depth > 1:
        for value in struct.values():
            if isinstance(value, dict):
                result = find_key(value, k, depth - 1)
                if result:
                    break
        else:
            result = None
        return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
flag_d = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if flag_d == 'y':
    m_depth = int(input('Введите максимальную глубину: '))
    found_k = find_key(site, key, m_depth)
elif flag_d == 'n':
    found_k = find_key(site, key, )
print('Значение ключа: {}'.format(found_k))
