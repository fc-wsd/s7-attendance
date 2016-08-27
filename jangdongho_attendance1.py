from datetime import datetime

attendances = {}

def attend(students):
    for student in students:
        attendances[student] = datetime.today()

def show_today_attend():
    print(attendances.items())

students = ('장동호', '학생1', '학생2', '학생3') # 수강생이름들을 어디서 확인할 수 있나요?
attend(students)
show_today_attend()
