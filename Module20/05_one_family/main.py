family = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Иванов', 'Антон'): 14,
    ('Петровна', 'Анна'): 25,
    ('Иванова', 'Ульяна'): 31,
    ('Сидоров', 'Павел'): 10,
    ('Иванов', 'Кирил'): 70
}

need_surname = input('Введите фамилию: ')

for surname, name in family.keys():
    if surname.lower() == need_surname.lower():
        print(surname, name, family[surname, name])
    elif surname.lower()[:-1] == need_surname.lower():
        print(surname, name, family[surname, name])