def my_zip(*args):
    return [tuple(arr[i] for arr in args) for i in range(min(map(len, args)))]


# string = input('Строка: ')
# tp = (int(x) for x in input('Кортеж чисел: ').split())
# lst_tp = list(tp)
# new_tpl = my_zip(string, lst_tp)
# print(new_tpl)
