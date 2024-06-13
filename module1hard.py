# Задание "Средний балл"

# Исходные данные задачи 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Рассчет среднего арифметического c помощью индексации, метода sum и len, создание списка средних арифметических
average = list(((sum(grades[0][0::])/len(grades[0][0::])), (sum(grades[1][0::])/len(grades[1][0::])),
                (sum(grades[2][0::])/len(grades[2][0::])), (sum(grades[3][0::])/len(grades[3][0::])),
                (sum(grades[4][0::])/len(grades[4][0::]))))

# Сортировка студентов в алфавитном порядке
Sort_stud = list(students)  # Изменим тип с множества (set) на список (list) и присвоим собственное имя переменной
Sort_stud.sort()  # произведем сортировку списка (которая возможна только в списке!)

# Создаем словарь воспользовавшись методом dict и итерации zip и выводим
# Методы dict и zip взяты отсюда: https://docs.python.org/3/library/functions.html,
# изучены по инфомации в интернете, проверены эмпирическим путем
dictionary = dict(zip(Sort_stud, average))
print(dictionary)
