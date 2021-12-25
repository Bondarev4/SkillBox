def site_copy(struct, product):
    if 'title' in struct:
        struct['title'] = 'Куплю/продам {} недорого'.format(product)
    if 'h2' in struct:
        struct['h2'] = 'У нас самая низкая цена на {}'.format(product)
    for value in struct.values():
        if isinstance(value, dict):
            site_copy(value, product)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
# n = int(input('Сколько сайтов: '))
# n_site = {}
# for i in range(n):
#     name_of_product = input('Введите название продукта для нового сайта: ')
#     site_copy(site, name_of_product)
#     print('\nСайт для {}:\n'.format(name_of_product), site)
