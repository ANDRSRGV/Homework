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
            print (123)
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        # print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{avg_grade(self.grades)}')
        # print(*self.courses_in_progress,', ')

        student_to_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{avg_grade(self.grades)}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'
        return(student_to_print)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
    grade_options = (1,2,3,4,5,6,7,8,9,10)
    def __str__(self):
        lecturer_to_print= f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade(self.grades)}'
        return(lecturer_to_print)


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



st = Student('Alan','Berns','male')
rev = Reviewer('Bob','Smith')
lect = Lecturer('Sam', 'Fisher')

st.courses_in_progress.append('course1')
st.courses_in_progress.append('course2')
st.finished_courses.append('A')
rev.courses_attached.append('course1')
rev.courses_attached.append('course2')
lect.courses_attached.append('course1')
lect.courses_attached.append('course2')
rev.rate_hw(st, 'course1', 1)
rev.rate_hw(st, 'course2', 4)
st.rate_lecturer(lect, 'course1', 1)
st.rate_lecturer(lect, 'course1', 3)
st.rate_lecturer(lect, 'course2', 5)

print(st.grades)
print(st.courses_in_progress)
print(lect.grades)
print(rev)

print( avg_grade(lect.grades))
print (lect)
print (st)