students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(stds):
    lst = []
    cnt = 0
    for value in stds.values():
        lst += value['interests']
        cnt += len(value['surname'])
    return lst, cnt


pairs = []

for i, value in students.items():
    pairs.append((i, value['age']))

print('Список пар "ID студента - Возраст":', pairs)

my_int, letters = f(students)
print('Полный список интересов всех студентов:', my_int,
      '\nОбщая длина всех фамилий студентов:', letters)

