from datetime import datetime

attendances = {}
# 출석자 명단

students = ['고병남', '장동호', '신성욱', '임재민', '권혁기', '김재국', '이서준', '김민수', '여현구',]
# 학생 명단

def attend(*attend_list):
    for key in attend_list:
        if key in students:
        # 학생 명단에 있는지 체크

            if key in attendances.keys():
            # 기 출석여부 체크
                print(key+" 은 이미 출석하였습니다.")
            else :
            # 출석 등록
                attendances[key] = [datetime.now().strftime("%Y/%m/%d %H:%M:%S"),]
        else :
            print("학생 명단에 없습니다")

def show_attendances_list() :
    for key in attendances.keys():
        comment = '{name} 은{datetime} 에 출석하였습니다.'.format(name=key, datetime=attendances[key][0])
        print(comment)

attend("홍길동")
# 개별 출석처리

attend(*students)
# 단체 출석처리

show_attendances_list()
# 출석확인

