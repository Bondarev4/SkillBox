shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
quantity = 0
sum_prize = 0
for i in range(len(shop)):
        if shop[i][0] == detail:
                quantity += 1
                sum_prize += shop[i][1]
print('\nКол-во деталей -', quantity)
print('Общая стоимость -', sum_prize)