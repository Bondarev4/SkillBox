def analysis_text(text):
    t_a = open('analysis.txt', 'w')
    letters = {}
    for letter in text.read().lower():
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    sort_letters = {el: letters[el] for el in sorted(letters, key=letters.get, reverse=True)}
    sum_letter = sum(sort_letters.values())
    for sym, count in sort_letters.items():
        t_a.write(sym + ' ' + str(round((count / sum_letter), 3)) + '\n')
    t_a.close()


file_text = open('text.txt', 'r')
print('Содержимое файла text.txt:')
print(file_text.read())

file_text = open('text.txt', 'r')
analysis_text(file_text)

file_analysis = open('analysis.txt', 'r')
print('\nСодержимое файла analysis.txt:')
print(file_analysis.read())

file_text.close()
file_analysis.close()