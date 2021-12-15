def is_prime(x):
    d = 2
    while d * d <= x and x % d != 0:
        d += 1
    return d * d > x

def arr(box):
    return [value for i, value in enumerate(box) if is_prime(i)]
