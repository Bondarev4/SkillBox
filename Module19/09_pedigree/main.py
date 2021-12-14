number = int(input('Введите количество человек: '))
members = dict()
first_p, second_p = input('1 пара: ').split()
members[second_p] = 0
members[first_p] = members[second_p] + 1
for i in range(2, number):
    first_p, second_p = input(str(i) + ' пара: ').split()
    members[first_p] = members[second_p] + 1
print('\n“Высота” каждого члена семьи:')
for name in sorted(members):
    print(name, members[name])