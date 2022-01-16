file = open('numbers.txt', 'r')
s = 0
for string in file:
    s += sum(map(int, string.split()))
print('Содержимое файла answer.txt')
file.close()
print(s)