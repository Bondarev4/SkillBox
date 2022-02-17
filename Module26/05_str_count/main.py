import os
from pathlib import Path


def strings_in(directory):
    for file in os.listdir(directory):
        counter = 0
        if Path(file).suffixes[0] == '.py':
            with open(file, 'r') as str_file:
                for string in str_file:
                    string = string.split()
                    if len(string) != 0 and string[0] != '#':
                        counter += 1
                    # print(string, counter, sep='------')  # check
            yield counter
    return


#
#
my_directory = os.path.abspath('')
for count in strings_in(my_directory):
    print(count)
