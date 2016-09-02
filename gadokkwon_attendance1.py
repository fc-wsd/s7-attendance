# 과제1
# 권혁기

import datetime 
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')


students = ['장동호','신성욱','임재민','권혁기','김재국']


attendances = {};


def attend():
	print('출첵하세요')
	student = input()
	if student in students:
		attendances.update({student : nowDatetime })
		print(attendances)
	else:
		print('학생이 아닙니다.')

attend()
