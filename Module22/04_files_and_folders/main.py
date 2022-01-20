import os


def calculate(directory, size=0, catalogs=0, files=0):
    print(directory)
    for el in os.listdir(directory):
        path_el = os.path.join(directory, el)
        if os.path.isdir(path_el):
            catalogs += 1
            calculate(path_el, size, catalogs, files)
        else:
            size += os.path.getsize(path_el)
            files += 1
    return size, catalogs, files


path = input('Пожалуйста, введите путь до директории: ')
s_size, s_catalogs, s_files = calculate(path)
print('Размер каталога (в Кб): {}\nКоличество подкаталогов: {}\nКоличество файлов: {}'.format(s_size,
                                                                                              s_catalogs,
                                                                                              s_files))
