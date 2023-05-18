groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Аркадий",
        "surname": "Фокин",
        "exams": ["Математика", "Химия", "ОБЖ"],
        "marks": [2, 4, 3]
    },
    {
        "name": "Михаил",
        "surname": "Быковский",
        "exams": ["Геометрия", "ИЗО", "Физика"],
        "marks": [3, 5, 3]
    },
]


def filter_students_by_avg_mark(students):
    # Запрос средней оценки у пользователя
    avg_mark = float(input("Введите средний балл для фильтрации студентов: "))

    # Фильтрация списка студентов по средней оценке
    filtered_students = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= avg_mark:
            filtered_students.append(student)

    # Вывод отфильтрованного списка студентов
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in filtered_students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))
# Вызов функции фильтрации студентов по средней оценке
filter_students_by_avg_mark(groupmates)