def max_elem(a):
    max_el = a[0]
    for x in a:
        if x > max_el:
            max_el = x
    return max_el


old_l = [3070, 2060, 3090, 3070, 3090]
new_l = []
sell_el = max_elem(old_l)
for card in old_l:
    if card != sell_el:
        new_l.append(card)
print('Старый список видеокарт:', old_l, '\nНовый список видеокарт:', new_l)