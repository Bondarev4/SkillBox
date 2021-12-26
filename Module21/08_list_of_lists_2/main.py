def reveal_lst(lst, n_lst):
    for el in lst:
        if isinstance(el, list):
            reveal_lst(el, n_lst)
        else:
            n_lst.append(el)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_lst = list()
reveal_lst(nice_list, new_lst)
print(new_lst)
