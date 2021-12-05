name = input('Название файла: ')
start = '@№$%^&*()'
if name[0] in start:
    print('\nОшибка: название начинается на один из специальных символов')
elif not name.endswith('.txt' or '.docx'):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('\nФайл назван верно.')