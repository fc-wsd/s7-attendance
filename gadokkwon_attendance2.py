# 과제2
# 권혁기

import datetime 
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')


students = ['장동호','신성욱','임재민','권혁기','김재국']




class Student():
	def __init__(self):
		self.name = name
		self.attendance = ""
		self.nowDatetime = nowDatetime



class Attendance(Student):

	def attend(self):
		super().__init__(name)
		self.attendance = "출석"
		print("aaaa")

	def list(self):
		for i in students :
			if students[i] == name :
				print(i)
			else :
				print(students)


line = "-"* 40
print(line)
print('출첵하세요')
name = input()



while name :
	student = Attendance()
	student.attend()
	student.list(name)
	if len(name) == 0:
		break














