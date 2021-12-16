def check_numbers(a):
    for x in a:
        if int(x) != x:
            return False
    return True

def sort(tpl):
    if not check_numbers(tpl):
        return False
    tpl = list(tpl)
    j = 1
    n = len(tpl)
    while j < n:
        for i in range(n - j):
            if tpl[i] > tpl[i + 1]:
               tpl[i], tpl[i + 1] = tpl[i + 1], tpl[i]
        j += 1
    return tuple(tpl)

