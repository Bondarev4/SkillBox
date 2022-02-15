from collections.abc import Iterator


def found_number(lst_1: list, lst_2: list, to_f: int) -> Iterator:
    for n_1 in lst_1:
        for n_2 in lst_2:
            yield n_1, n_2, n_1 * n_2
            if n_1 * n_2 == to_f:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for x, y, result in found_number(lst_1=list_1, lst_2=list_2, to_f=to_find):
    print(x, y, result)
