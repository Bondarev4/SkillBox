import random

first_t = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_t = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [first_t[i] if first_t[i] > second_t[i] else second_t[i] for i in range(20)]
print('Первая команда:', first_t)
print('Вторая команда:', second_t)
print('Победители тура:', winners)
