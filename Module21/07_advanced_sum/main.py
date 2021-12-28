def sum_p(*args):
    s = 0
    for element in args:
        if isinstance(element, int):
            s += element
        else:
            for i, v in enumerate(element):
                s += sum_p(v)
    return s


# print(sum_p([[1, 2, [3]], [1], 3]))
# print((sum_p(1, 2, 3, 4, 5)))