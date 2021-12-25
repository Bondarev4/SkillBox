def mega_sum(*args):
    s = 0
    for element, i in enumerate(args):
        if isinstance(element, int):
            s += element
        else:
            s += mega_sum(element[i])
    return s


print(mega_sum([[1, 2, [3]], [1], 3]))
# print(mega_sum(1, 2, 3, 4, 5))
