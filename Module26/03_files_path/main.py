import os
from collections.abc import Iterator


def gen_files_path(search_directory, current_catalog) -> Iterator:
    if os.path.basename(current_catalog) == search_directory:
        print('Found!!')
        exit()
    catalogs = os.listdir(current_catalog)
    for element in catalogs:
        path = os.path.join(current_catalog, element)
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            for file_path in gen_files_path(search_directory, path):
                print(file_path)


your_catalog = input('Укажите каталог для поиска: ')
directory = input('Укажите начальную директорию, для отмены напишите "0": ')
if directory == '0':
    directory = os.path.abspath(os.sep)
for i in gen_files_path(your_catalog, directory):
    pass

# При проходе по корневому диску [WinError 5] Отказано в доступе: 'C:\\$Recycle.Bin\\S-1-5-18'
# PermissionError: [WinError 5] Отказано в доступе: 'C:\\AdwCleaner'.
