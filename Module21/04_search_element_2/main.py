def dict_depth(dic, level=1):
    if not isinstance(dic, dict) or not dic:
        return level
    return max(dict_depth(dic[ke], level + 1) for ke in dic)

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
else:
    found_k = find_key(site, key, dict_depth(site))
print('Значение ключа: {}'.format(found_k))
