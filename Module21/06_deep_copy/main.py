def site_copy(struct, product):
    if 'title' in struct:
        struct['title'] = 'Куплю/продам {} недорого'.format(product)
    if 'h2' in struct:
        struct['h2'] = 'У нас самая низкая цена на {}'.format(product)
    for value in struct.values():
        if isinstance(value, dict):
            site_copy(value, product)

def s_p(struct, i=1):
    for k, v in struct.items():
        if isinstance(v, dict):
            print("{}'{}': ".format('\t'*i, k))
            s_p(v, i + 1)
        else:
            print("{}'{}': '{}'".format('\t'*(i+1), k, v))


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
# n_sites = {}
# for i in range(n):
#     name_of_product = input('\nВведите название продукта для нового сайта: ')
#     site_copy(site, name_of_product)
#     n_sites[name_of_product] = site
#     for key, value in n_sites.items():
#         print('Сайт для {}:\nsite ='.format(key))
#         s_p(value)

