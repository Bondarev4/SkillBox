def film_found(n, f):
    for name_f in f:
        if name_f == n:
            return True
    return False


n = int(input('Введите кол-во фильмов в вашем запросе: '))
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
your_best_films = []
for i in range(n):
    name = input('\nВведите название фильма: ')
    if film_found(name, films):
        your_best_films.append(name)
    else:
        print('Такого фильма у нас нет(')
print('\nВыбрынные фильмы:', *your_best_films)

