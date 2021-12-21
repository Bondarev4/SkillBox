def calculating_math_func(data):
    if data in fact:
        result = fact[data]
    else:
        result = 1
        for i in range(1, data + 1):
            result *= i
        fact[data] = result
    result /= data ** 3
    result = result ** 10
    return result


fact = dict()
