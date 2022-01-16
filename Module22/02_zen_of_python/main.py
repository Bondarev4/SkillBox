file = open('zen.txt', 'r')
for string in file.readlines()[::-1]:
    print(string, end='')
file.close()