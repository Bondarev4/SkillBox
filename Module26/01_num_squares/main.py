from collections.abc import Iterator


class Numbers:
    def __init__(self, number: int) -> None:
        self.__number = number
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__counter < self.__number:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration


def square(number: int) -> Iterator:
    for i in range(1, number + 1):
        yield i ** 2


n = int(input('Введите число: '))

class_iter = Numbers(number=n)
for value in class_iter:
    print(value, end=' ')

print()

for value in square(number=n):
    print(value, end=' ')

print()

for element in [x ** 2 for x in range(1, n + 1)]:
    print(element, end=' ')
