from datetime import datetime

class Student(object):
# 학생 명단 클래스
    students = ['고병남', '장동호', '신성욱', '임재민', '권혁기', '김재국', '이서준', '김민수', '여현구',]

    def list(self):
    # 학생 명단 출력 메소드
        print(self.students)

    @classmethod
    def set_student_list(cls, *students):
    #학생 명단 추가 메소드
        for student in students:
            cls.students.append(student)

class Attendance(Student):
# 출석부 클래스

    attendances = {}

    def attend(self, *attend_list):
    # 출석 추가 메소드
        for key in attend_list:
            if key in Student.students:
            # 학생 명단에 있는지 체크

                if key in self.attendances.keys():
                # 기 출석여부 체크
                    print(key+" 은 이미 출석하였습니다.")
                    # 기출석자

                else :
                # 출석등록
                    self.attendances[key] = [datetime.now().strftime("%Y/%m/%d %H:%M:%S"),]
            else :
                print("학생 명단에 없습니다.")

    def list(self):
    # 출석자 명단 출력 메소드
        for key in self.attendances.keys():
            comment = '{name} 은 {datetime} 에 출석하였습니다.'.format(name=key, datetime=self.attendances[key][0])
            print(comment)


student = Student()
# 학생 명단 객체

student.set_student_list("홍길동")
# 학생 명단 추가

student.list()
# 학생 명단 출력

attendance = Attendance()
# 출석부 객체

attendance.attend('고병남','김재국')
# 개별 출석등록

attendance.attend(*student.students)
# 단체 출석등록

attendance.list()
# 출석자 명단 출력
