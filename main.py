class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self):
        if not self.grades:
            return 0
        list_grades = [] # создаем пустой спиcок
        for mark in self.grades.values():
            # проходимся по значениям словаря
            list_grades += mark
            # добавляем оценку в список
        return round(sum(list_grades) / max(len(list_grades), 1))

    def rate_hw(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grades <= 10:
                # Было бы решением, если не создание словаря - упрощенный вариант.
                # lecturer.grades_lecturer.append(student_grade_to_lecturer)
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):

        info_some_student = f'Имя: {self.name} \n' \
                            f'Фамилия: {self.surname}\n' \
                            f'Средняя оценка за домашние задания: {self.avg_grade()}\n' \
                            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
                            f'Завершенные курсы: {", ".join(self.finished_courses)}'
                            # c помощью .join объединяем список строк

        return info_some_student

    def __eq__(self, other) -> bool:
        if not isinstance (other, self.__class__):
            raise Exception('Ошибка')
            #Проверка на принадлежность к классу, чтобы не сравнивать сущности разных классов.
        return self.avg_grade() == other.avg_grade()

    def __lt__(self, other) -> bool:
        if not isinstance (other, self.__class__):
            raise Exception('Ошибка')
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other) -> bool:
        if not isinstance (other, self.__class__):
            raise Exception('Ошибка')
        return self.avg_grade() <= other.avg_grade()

class Reviewer(Mentor):
    # из родителя (Mentor) берётся self.name, self.surname и self.courses_attached

    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grades <= 10:
            # self.courses_attached - обращаемся к родителю (Ментор)
            # student.courses_in_progress - обращаемся к подклассу (Student)
            if course in student.grades:
                # если курс есть в журнале студента, то курс не добавляется, а добавляется оценка к слоту
                student.grades[course] += [grades]
                # student.grades[course] - ключ
            else:
                student.grades[course] = [grades]
        #     student.grades.append(grade)
        else:
           return 'Ошибка'

    def __str__(self):
        info_some_reviewer = f'Имя:{self.name} \nФамилия:{self.surname}'
        return info_some_reviewer


class Lecturer(Mentor, Student):
    # наследуем Student и "полиморфичем" avg_grade

    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __str__(self):
        info_some_lecturer = f'Имя:{self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}'
        return info_some_lecturer





#"<-----------Lecturer----------->
some_lecturer = Lecturer('Daniil', 'Cartockhin')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Java']
some_lecturer2 = Lecturer('Igor', 'Piotrovsky')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Java']
lecturer_list = [some_lecturer, some_lecturer2]
# cоздаем список для подсчета средней оценки за лекции всех лекторов в рамках курса
#<-------------------------------->
#"<-----------Reviewer----------->
some_reviewer = Reviewer('Vasilii', 'Pupkin')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Java']
some_reviewer2 = Reviewer('Ivan', 'Bogatirev')
some_reviewer2.courses_attached += ['Python']
some_reviewer2.courses_attached += ['Java']
#"<-----------Student----------->
some_student = Student('Steve', 'Jobs', 'M')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
some_student.finished_courses = ['Kotlin']
some_student2 = Student('Bill', 'Gates', 'M')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Java']
some_student2.finished_courses = ['Kotlin']
student_list = [some_student, some_student2]
# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
#<-------------------------------->

#"<-----------Student and his rate_hw----------->
some_student.rate_hw(some_lecturer, 'Python', 5)
some_student.rate_hw(some_lecturer2, 'Python', 5)
some_student.rate_hw(some_lecturer, 'Java', 10)
some_student.rate_hw(some_lecturer2, 'Java', 10)
some_student2.rate_hw(some_lecturer, 'Python', 5)
some_student2.rate_hw(some_lecturer2, 'Python', 5)
some_student2.rate_hw(some_lecturer, 'Java', 10)
some_student2.rate_hw(some_lecturer2, 'Java', 10)
#<-------------------------------->

#"<-----------Reviewer and his rate_hw----------->
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Java', 5)
some_reviewer.rate_hw(some_student2, 'Java', 5)
some_reviewer2.rate_hw(some_student, 'Python', 10)
some_reviewer2.rate_hw(some_student2, 'Python', 10)
some_reviewer2.rate_hw(some_student, 'Java', 5)
some_reviewer2.rate_hw(some_student2, 'Java', 5)
#<-------------------------------->

print('Students:')
print('-----------')
print(some_student)
print('-----------')
print(some_student2)
print()
print('Reviewers:')
print('-----------')
print(some_reviewer)
print('-----------')
print(some_reviewer2)
print()
print('Lectures:')
print('-----------')
print(some_lecturer)
print('-----------')
print(some_lecturer2)
print()


print('Средние оценки студентов за домашние задания одинаковые: ', some_student == some_student2)
print(f'Cредняя оценка {some_student.name} {some_student.surname} больше, чем у  {some_student2.name} {some_student2.surname}:', some_student > some_student2)
print(f'Cредняя оценка {some_student.name} {some_student.surname} меньше или равно, чем у {some_student2.name} {some_student2.surname:}:', some_student <= some_student2)

print('Средние оценки лекторов за лекции одинаковые: ', some_lecturer == some_lecturer2)
print(f'Cредняя оценка {some_lecturer.name} {some_lecturer.surname} больше, чем у  {some_lecturer2.name} {some_lecturer.surname}:', some_lecturer > some_lecturer2)
print(f'Cредняя оценка {some_lecturer.name} {some_lecturer.surname} меньше или равно, чем у {some_lecturer2.name} {some_lecturer.surname}:', some_lecturer <= some_lecturer2)

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# в качестве аргументов принимает список студентов и название курса.


def average_s_grade_on_the_course(persons, course):
    # в качестве аргументов принимаем список студентов (или лекторов) и название курса
    if not isinstance(persons, list):
        return 'Not list'
        # проверка принадлежности экземпляра к классу
    average_grade_course = []
    # вновь создаем пустой список
    for student in persons:
        average_grade_course += student.grades.get(course, [])
        # get возвращает значение по ключу (course) и записывает в average_grade_course = [], а course подается в print ниже
    if not average_grade_course:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(average_grade_course) / len(average_grade_course), 1)

def average_l_grade_on_the_course(persons, course):
    # в качестве аргументов принимаем список студентов (или лекторов) и название курса
    if not isinstance(persons, list):
        return 'Not list'
    average_grade_course = []
    # вновь создаем пустой список
    for lecturer in persons:
        # проходимся по элементам списка
        average_grade_course += lecturer.grades.get(course, [])
        # get возвращает значение по ключу (course) и записывает в average_grade_course = [], а course подается в print ниже
    if not average_grade_course:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(average_grade_course) / len(average_grade_course), 1)

print()
print('Общие средние оценки студентов и лекторов:')
print('----------------')
# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Java'}: {average_s_grade_on_the_course(student_list, 'Java')}")
print('----------------')
# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Java'}: {average_l_grade_on_the_course(lecturer_list, 'Java')}")

