max_n = int(input('Введите максимальное число: '))
numbers = set(range(1, max_n + 1))
while True:
    ans_b = input('\nНужное число есть среди вот этих чисел: ')
    if ans_b == 'Помогите!':
        ans_a = set(int(x) for x in input('Артём мог загадать следующие числа: ').split())
        numbers = ans_a & numbers
    else:
        ans_b = set(map(int, ans_b.split()))
        ans_a = input('Ответ Артёма: ')
        if ans_a == 'Да':
            if len(ans_b) == 1:
                print('\nБорис угадал число. Ура!')
                break
            else:
                numbers = numbers & ans_b
        else:
            numbers = numbers.difference(ans_b)