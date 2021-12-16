import random
arr = [random.randint(1, 10) for i in range(10)]
print('Оригинальный список:', arr)
arr = [(arr[i], arr[i + 1]) for i in range(0, len(arr) - 1, 2)]
print('Новый список:', arr)