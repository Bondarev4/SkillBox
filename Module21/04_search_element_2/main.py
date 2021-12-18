def found_key(struct, k, *args):
    # if args == 0:
    #     return None
    # if k in struct:
    #     return k, struct[k]
    args -= 1
    for key in struct.values():
        result = found_key(struct[key], k, *args)
        if result != 'None'
    return print('Значение ключа:', struct.get(key))

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
    found_k = found_key(site, key, m_depth)
else:
    found_k = found_key(site, key)
