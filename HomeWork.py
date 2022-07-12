def avg_grade(grades):
    grades_sum = 0
    grades_count = 0
    for grades_list in grades.values():
        grades_sum += sum(grades_list)
        grades_count += len(grades_list)
    return(grades_sum / grades_count)

class Student:
    def __init__(self, name, surname, gender ):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress\
        and grade in lecturer.grade_options:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        return (avg_grade(self.grades))
    def __lt__(self, std):
        if self.avg_grade() < std.avg_grade():
            return(True)
        else:
            return(False)
    def __str__(self):
        student_to_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{self.avg_grade()}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'
        return(student_to_print)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    grade_options = (1,2,3,4,5,6,7,8,9,10)
    def avg_grade(self):
        return (avg_grade(self.grades))
    def __str__(self):
        lecturer_to_print= f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return(lecturer_to_print)
    def __lt__(self, lec):
        if self.avg_grade() < lec.avg_grade():
            return(True)
        else:
            return(False)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')



st1 = Student('Alan','Berns','male')
st2 = Student('Bob', 'Marley','male')
rev1 = Reviewer('Bob','Smith')
rev2 = Reviewer('Tom','Log')
lect1 = Lecturer('Sam', 'Fisher')
lect2 = Lecturer('Tim', 'Dalton')

st1.courses_in_progress.append('course2')
st1.courses_in_progress.append('course3')
st1.finished_courses.append('Course1')
st2.courses_in_progress.append('course2')
rev1.courses_attached.append('course2')
rev2.courses_attached.append('course2')
rev2.courses_attached.append('course3')
lect1.courses_attached.append('course2')
lect1.courses_attached.append('course3')
lect2.courses_attached.append('course2')
rev1.rate_hw(st1, 'course2', 1)
rev2.rate_hw(st1, 'course2', 4)
rev1.rate_hw(st1, 'course3', 2)
rev2.rate_hw(st1, 'course3', 10)
rev1.rate_hw(st2, 'course2', 3)
rev2.rate_hw(st2, 'course2', 1)
st1.rate_lecturer(lect1, 'course2', 5)
st1.rate_lecturer(lect1, 'course3', 6)
st1.rate_lecturer(lect2, 'course2', 10)
st1.rate_lecturer(lect2, 'course3', 9)
st2.rate_lecturer(lect1, 'course2', 8)
st2.rate_lecturer(lect1, 'course3', 9)
print(f'Студент 1\n', st1)
print(f'Студент 2\n', st2)
print('Студент 1 успевает лучше студента 2:', st1>st2)

print(f'Лектор 1\n',lect1)
print(f'Лектор 2\n',lect2)
print('Лектор 1 более популярный, чем лектор 2:', lect1>lect2)

def avg_course_grade(students, course_name):
    grades_sum = 0
    grades_num = 0
    for st in students:
        if isinstance(st, Student):
          course_grades = st.grades[course_name]
          grades_sum += sum(course_grades)
          grades_num += len(course_grades)
    print(f'Средняя оценка студентов за курс \"{course_name}\": {grades_sum/grades_num}')

avg_course_grade([st1,st2],'course2')

def avg_lecturer_grade(lecturers, course_name):
    grades_sum = 0
    grades_num = 0
    for lec in lecturers:
        if isinstance(lec, Lecturer):
          course_grades = lec.grades[course_name]
          grades_sum += sum(course_grades)
          grades_num += len(course_grades)
    print(f'Средняя оценка лекторов за курс \"{course_name}\": {grades_sum/grades_num}')

avg_lecturer_grade([lect1, lect2], 'course2')