# 2016.09.01 김민수. 패스트 캠퍼스 과제 제출 정리파일
#
# 모델을 사용하지 않은 views.py 파일. 메모리에 학생정보 리스트와 출석정보 리스트 객체를 들고있다. (전역)
#
# 브라우저에서 새로고침을 할 때마다 4개씩 계속 늘어난다. 서버를 재시작하면 처음 4개만 출력된다.

# 패스트 캠퍼스 과제파일 시작 =================================================================================================

# App views.py =========================================================================================================

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# 출석학생 저장 리스트 객체
attendances = []

# 학생정보 리스트 객체
students = [
	{
		'student_age': 20,
		'student_tel': '010-0000-0000',
		'student_etc': '첫 번째 학생의 데이터입니다. 메모리에 올라갑니다.',
		'student_name': '첫 번째 학생',
		'student_email': 'email1@example.com'
	},
	{
		'student_age': 22,
		'student_tel': '010-0000-0001',
		'student_etc': '두 번째 학생의 데이터입니다. 메모리에 올라갑니다.',
		'student_name': '두 번째 학생',
		'student_email': 'email2@example.com'
	},
	{
		'student_age': 24,
		'student_tel': '010-0000-0002',
		'student_etc': '세 번째 학생의 데이터입니다. 메모리에 올라갑니다.',
		'student_name': '세 번째 학생',
		'student_email': 'email3@example.com'
	},
	{
		'student_age': 27,
		'student_tel': '010-0000-0003',
		'student_etc': '네 번째 학생의 데이터입니다. 메모리에 올라갑니다.',
		'student_name': '네 번째 학생',
		'student_email': 'email4@example.com'
	}
]

# attend 함수 : 들어온 인자가 리스트 객체이고 아이템이 0개 이상일 경우, 출석정보를 attendances 객체에 저장한다.
def attend(arr_students = []):
	if isinstance(arr_students, list) and len(arr_students) > 0:
		for student in arr_students:
			attendances.append(student)

# getMainPage 함수 : 템플릿 화면에 학생정보를 출력하는 함수. 학생정보는 메모리에 올라간다.
def getMainPage(req):

	# 글로벌 변수 선언
	global students
	global attendances

	# attend 함수 실행 학생 출석정보 추가
	attend(students)

	# 랜더링 데이터 객체 생성.
	tmp = {}
	tmp['arr_student'] = attendances
	return render(req, 'attendance_list.html', tmp)

# 패스트 캠퍼스 과제코드 끝 ==================================================================================================