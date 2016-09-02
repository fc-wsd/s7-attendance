class Student:
    def __init__(self, name):
	    self.name = name


class Attendance:
    def __init__(self, students):
        self.students = students
    def attend(self, student):
        self.students.append(student)
    def list(self):
        for i in range(len(self.students)):
            print ("이름: " + self.students[i].name)
            	


attendance = Attendance([]);
attendance.attend(Student("김재국"))
attendance.attend(Student("고병남"))
attendance.attend(Student("이서준"))
attendance.attend(Student("차경묵"))
attendance.attend(Student("유보미"))
attendance.list();

