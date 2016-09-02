# 2016.09.01 김민수. 패스트 캠퍼스 과제 제출 정리파일
#
# 모델을 사용한 views.py, models.py 파일. 이 프로젝트는 sqlite3 에 테이블을 생성하여 저장한다.
# 서버 실행 시, 최초 4개의 학생데이터가 출력되며 새로고침 및 서버를 재시작 할 때마다 4개씩 데이터가 추가된다.

# 패스트 캠퍼스 과제파일 시작 =================================================================================================

# App models.py ========================================================================================================

from django.db import models
from django.conf import settings

class Student(models.Model):

	student_age = models.IntegerField()
	student_tel = models.CharField(max_length=11)
	student_etc = models.TextField()
	student_name = models.CharField(max_length=20, blank=False, null=False)
	student_email = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

# App views.py =========================================================================================================

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from att_list.models import Student

class Attendance(View):

	students = [
		{
			'student_age' : 20,
			'student_tel' : '010-0000-0000',
			'student_etc' : '첫 번째 학생의 데이터입니다. 순위가 변경될 수 있습니다.',
			'student_name' : '첫 번째 학생',
			'student_email' : 'email1@example.com'
		},
		{
			'student_age': 22,
			'student_tel': '010-0000-0001',
			'student_etc': '두 번째 학생의 데이터입니다. 순위가 변경될 수 있습니다.',
			'student_name': '두 번째 학생',
			'student_email': 'email2@example.com'
		},
		{
			'student_age': 24,
			'student_tel': '010-0000-0002',
			'student_etc': '세 번째 학생의 데이터입니다. 순위가 변경될 수 있습니다.',
			'student_name': '세 번째 학생',
			'student_email': 'email3@example.com'
		},
		{
			'student_age': 27,
			'student_tel': '010-0000-0003',
			'student_etc': '네 번째 학생의 데이터입니다. 순위가 변경될 수 있습니다.',
			'student_name': '네 번째 학생',
			'student_email': 'email4@example.com'
		}
	]

	# init 함수 : 생성자 함수입니다. 멤버변수에 저장된 학생정보를 attend 함수에 전달합니다.
	def __init__(self):
		# 생성사가 호출되면 attend 메서드가 실행됩니다
		self.attend(self.students)

	# addStudent 함수 : 학생 리스트가 전달되면, 반복문으로 학생정보를 DB에 추가합니다.
	def attend(self, arr_student):

		# arr_student 파라미터가 리스트라면, sqlite3 DB에 4명의 학생정보를 추가합니다. 서비스가 재실행 될 때마다 정보가 추가됩니다.
		if isinstance(arr_student, list):
			for std in arr_student:
				obj_student = Student()
				obj_student.student_age = std['student_age']
				obj_student.student_tel = std['student_tel']
				obj_student.student_etc = std['student_etc']
				obj_student.student_name = std['student_name']
				obj_student.student_email = std['student_email']

				obj_student.save()

	# list 함수 : DB에 저장된 학생정보를 출력합니다. 템플릿과 연계되어 출력될 수 있습니다.
	def list(self):
		arr_studentlist = Student.objects.all().order_by('-student_name')
		return arr_studentlist

	# get 함수 : 이 예제에서 POST 방식은 따로 설정하지 않았습니다.
	def get(self, req):

		arr_student = self.list()

		tmp = {}
		tmp['arr_student'] = arr_student
		return render(req, 'attendance_list.html', tmp)

# 패스트 캠퍼스 과제코드 끝 ==================================================================================================