def site_copy(struct, product, new_site):
    if 'title' == struct:
        new_site['title'] = 'Куплю/продам {} недорого'.format(product)
    elif 'h2' == struct:
        new_site['h2'] = 'У нас самая низкая цена на {}'.format(product)
    else:
        new_site[struct] = site[struct]
    for value in struct.values():
        if isinstance(value, dict):
            return site_copy(value, product, new_site)
    return new_site


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
n = int(input('Сколько сайтов: '))
n_site = {}
for i in range(n):
    name_of_product = input('Введите название продукта для нового сайта: ')
    print(site, name_of_product, n_site)
