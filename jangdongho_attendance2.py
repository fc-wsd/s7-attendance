from datetime import datetime

class Student(object):
    name = ''
    attend_date = ''

    def set_info(self, name, attend_date):
        self.name = name
        self.attend_date = attend_date

class Attendance(object):
    attend_student_list = []

    def attend(self, student):
        self.attend_student_list.append(student)

    def list(self):
        for attend_student in self.attend_student_list:
            show = '{name}님은 {date} 에 출석함'.format(name=attend_student.name, date=attend_student.attend_date)
            print(show)

attendance = Attendance()
student_name_list = ['장동호', '학생1', '학생2', '학생3']
for name in student_name_list:
    student = Student()
    student.set_info(name, datetime.today())
    attendance.attend(student)

attendance.list()
