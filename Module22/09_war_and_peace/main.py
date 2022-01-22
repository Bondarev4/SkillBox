import zipfile


my_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
my_zip.extractall()

text = open('voyna-i-mir.txt', 'r', encoding='UTF-8')
letters = dict()

for letter in text.read():
    if letter.isalpha():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
sort_letters = {el: letters[el] for el in sorted(letters, key=letters.get, reverse=True)}

statistic = open('Stat.txt', 'w')
for symbol, count in sort_letters.items():
    statistic.write(symbol + ' - ' + str(count) + '\n')

statistic.close()
text.close()