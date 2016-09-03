
students = ['이서준', '고병남', '김재국']

class Student:
    def __init__(self, name):
        self.name = name

class Attendance():
    attended_students = []
    def attend(self, student):
        self.attended_students.append(student)
        print("%s 출석했습니다." % student.name)
    def list(self):
        for i in range(len(self.attended_students)):
            print("출석자 %s" % (self.attended_students[i].name))


attendance = Attendance()

attendance.attend(Student("이서준"))
attendance.attend(Student("고병남"))
attendance.attend(Student("김재국"))

attendance.list()



