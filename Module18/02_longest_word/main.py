string = input('Введите строку: ').split()
max_long = len(string[0])
this_word = string[0]
for word in string:
    n = len(word)
    if n > max_long:
        max_long = n
        this_word = word
print(this_word)