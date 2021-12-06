def countnum(a):
    c = 0
    for sim in a:
        if sim.isdigit():
            c += 1
    return c >= 3
def isup(a):
    for sim in a:
        if sim.isupper():
            return True
    return False


while True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8 and isup(password) and countnum(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
