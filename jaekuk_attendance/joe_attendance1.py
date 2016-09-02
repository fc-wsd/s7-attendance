def attend (name, date):
    global list_attendances
    if (date not in list_attendances):
        list_attendances[date] = []
    list_attendances[date].append(name);
    return list_attendances

list_attendances = {}   # 출근기록부
students = '김재국', '고병남', '이서준', '차경묵', '유보미'     # 학생리트스 
list_attendances = attend(students[0], '2016-09-02')
list_attendances = attend(students[1], '2016-09-02')
list_attendances = attend(students[3], '2016-09-02')
list_attendances = attend(students[4], '2016-09-02')


list_attendances = attend(students[0], '2016-09-03')
list_attendances = attend(students[1], '2016-09-03')
list_attendances = attend(students[2], '2016-09-03')
list_attendances = attend(students[4], '2016-09-03')

print (list_attendances)





