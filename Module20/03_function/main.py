def new_tur(t, x):
    if x not in t:
        return tuple()
    if t.count(x) < 2:
        return t[t.index(x):]
    x_f = t.index(x)
    return t[x_f:t[x_f + 1:].index(x) + x_f + 2]