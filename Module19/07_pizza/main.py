n = int(input('Введите кол-во заказов: '))
delivery = {}
for i in range(1, n + 1):
    order = input(str(i) + ' заказ: ').split()
    name = order[0]
    type = order[1]
    quantity = int(order[2])
    if name not in delivery:
        delivery[name] = dict()
        delivery[name][type] = quantity
    elif type not in delivery[name]:
        delivery[name][type] = quantity
    else:
        delivery[name][type] += quantity
print()
for name_key in delivery.keys():
    print(''.join([name_key, ':']))
    for type_key in delivery[name_key].keys():
        print(''.join(['\t', type_key, ':']), delivery[name_key][type_key])