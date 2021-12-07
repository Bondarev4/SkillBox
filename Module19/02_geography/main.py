n = int(input('Кол-во стран: '))
countries = dict()
for i in range(1, n + 1):
    country = input(' '.join([str(i), 'страна: '])).split()
    countries[country[0]] = country[1:]
cities = countries.values()
for j in range(1, 4):
    city = input(' '.join([str(j), 'город: ']))
    for key in countries.keys():
        flag = False
        if city in countries[key]:
            print('Город', city, 'расположен в стране', key)
            flag = True
            break
    if not flag:
        print('По городу', city, 'данных нет.')



