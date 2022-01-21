import os


def calculate(directory, size=0, catalogs=0, files=0):
    print(directory, size, catalogs, files)
    for el in os.listdir(directory):
        path_el = os.path.join(directory, el)
        if os.path.isdir(path_el):
            catalogs += 1
            s, c, f = calculate(path_el)
            files += f
            catalogs += c
            size += s
        else:
            size += os.path.getsize(path_el)
            files += 1
    return size, catalogs, files
# C:\SkillBox\pythonProject\Python_Basic\Module14

path = input('Пожалуйста, введите путь до директории: ')
s_size, s_catalogs, s_files = calculate(path)
print('Размер каталога (в Кб): {}\nКоличество подкаталогов: {}\nКоличество файлов: {}'.format(s_size / 1024,
                                                                                              s_catalogs,
                                                                                              s_files))
