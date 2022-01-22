def count_second_tour(file, n):
    s_t = open('second_tour.txt', 'w')
    s_t.write(str(n) + '\n')
    score = {}
    for line in file:
        elements_l = line.split()
        if len(elements_l) > 2:
            score[int(elements_l[2])] = elements_l[0][0] + '. ' + elements_l[1]
    for i, element in enumerate(reversed(sorted(score.items()))):
        if i == n:
            break
        s_t.write(str(i + 1) + ') ' + element[1] + ' ' + str(element[0]) + '\n')
    s_t.close()


first_file = open('first_tour.txt', 'r')
print('Содержимое файла first_tour.txt:')
print(first_file.read())

first_file = open('first_tour.txt', 'r')
count_second_tour(first_file, 2)

second_file = open('second_tour.txt', 'r')
print('\nСодержимое файла second_tour.txt:')
print(second_file.read())

first_file.close()
second_file.close()