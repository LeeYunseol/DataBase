import pymysql
from tkinter import *
#★각 함수의 비밀번호(PASSWORD)는 본인 MYSQL의 ROOT(ROOT가 아니면 ROOT도 수정)의 비밀번호로 변경하셔야합니다.★

#특징 호출 함수
def showdata_characteristic() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    sql = "select * from 상세특징 where 특징_강의_교과번호='{}' and 특징_교수_교수번호='{}'".format(lec_no, prof_no)
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 교과번호 : " + str(row[1]) + ", 학번 : " + str(row[2]) + ", 말빠르기 : " + str(
            row[3]) + ", 목소리 크기 : " + str(row[4]) + ", 이해정도확인여부 : " + str(row[5]) + ", 강의시간초과여부 : " + str(row[6]) + ", 강의력 : " + str(row[7]))
        row = cur.fetchone()
    print()
    conn.close()
#과제 호출 함수
def showdata_assignmnet():
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    sql = "select * from 과제상세 where 과제_강의_교과번호='{}' and 과제_교수_교수번호='{}'".format(lec_no, prof_no)
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 교과번호 : " + str(row[1]) + ", 학번 : " + str(row[2]) + ", 텀프로젝트 : " + str(
            row[3]) + ", 개인과제 : " + str(row[4]))
        row = cur.fetchone()
    print()
    conn.close()
#시험성적 호출 함수
def showdata_test():
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    sql = "select * from 시험성적상세 where 시험성적_강의_교과번호='{}' and 시험성적_교수_교수번호='{}'".format(lec_no, prof_no)
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 교과번호 : " + str(row[1]) + ", 학번 : " + str(row[2]) + ", 플러스여부 : " + str(
            row[3]) + ", 시험출제 스타일 : " + str(row[4]) + ", 퀴즈여부 : " + str(row[5]))
        row = cur.fetchone()
    print()
    conn.close()

#강의스타일 호출 함수
def showdata_style():
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    sql = "select * from 상세강의스타일 where 강의스타일_강의_교과번호='{}' and 강의스타일_교수_교수번호='{}'".format(lec_no, prof_no)
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 교과번호 : " + str(row[1]) + ", 학번 : " + str(row[2]) + ", 교재 : " + str(
            row[3]) + ", 강의방법 : " + str(row[4]) + ", 출석체크 : " + str(row[5]) + ", 원어 : " + str(row[6]) + ", 강의스타일 : " + str(row[7]))
        row = cur.fetchone()
    print()
    conn.close()

#학생 정보 입력 함수
def insert_student_information() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    inserted_student_id = str(student_id.get())
    inserted_student_major = str(student_major.get())
    inserted_student_name  = str(student_name.get())


    sql = "insert into 학생 values ('{}', '{}', '{}')".format(inserted_student_id, inserted_student_major,inserted_student_name)

    cur.execute(sql)

    conn.commit()

#시험성적 정보 입력하는 함수
def insert_test() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    inserted_student_id = str(student_id.get())
    inserted_plus_or_not = str(plus_or_not.get())
    inserted_test_style = str(test_style.get())
    inserted_quiz_or_not = str(quiz_or_not.get())


    sql = "insert into 시험성적상세(시험성적_교수_교수번호, 시험성적_강의_교과번호, 평가_학생_학번, 플러스여부, 시험출제스타일, 퀴즈여부) values ('{}', " \
          "'{}', '{}', '{}', '{}', '{}')".format(prof_no,lec_no, inserted_student_id, inserted_plus_or_not,
                                                       inserted_test_style,inserted_quiz_or_not)
    cur.execute(sql)

    conn.commit()
#과제 정보 입력하는 함수
def insert_assignment() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    inserted_student_id = str(student_id.get())
    inserted_term_project = str(term_project.get())
    inserted_private_assignment = str(private_assignment.get())

    sql = "insert into 과제상세(과제_교수_교수번호, 과제_강의_교과번호, 평가_학생_학번, 텀프로젝트, 개인과제) values ('{}', " \
          "'{}', '{}', '{}', '{}')".format(prof_no, lec_no, inserted_student_id, inserted_term_project, inserted_private_assignment)
    cur.execute(sql)

    conn.commit()

#특징 정보 입력하는 함수
def insert_characteristic() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    inserted_student_id = str(student_id.get())
    inserted_speacking_rate = str(speaking_rate.get())
    inserted_voice = str(voice.get())
    inserted_check_understanding = str(check_understanding.get())
    inserted_lecture_time = str(lecture_time.get())
    inserted_teaching = str(teaching.get())
    sql = "insert into 상세특징(특징_교수_교수번호, 특징_강의_교과번호, 평가_학생_학번, 말빠르기, 목소리크기, 이해정도확인여부, 강의시간초과여부, 강의력) values ('{}', " \
          "'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(prof_no, lec_no, inserted_student_id,inserted_speacking_rate, inserted_voice,inserted_check_understanding,inserted_lecture_time,inserted_teaching)
    cur.execute(sql)

    conn.commit()

#강의스타일 정보 입력하는 함수
def insert_style() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                          , db='termproject', charset='utf8')
    cur = conn.cursor()
    lec_no = str(lecture_number.get())
    prof_no = str(professor_number.get())
    inserted_student_id = str(student_id.get())
    inserted_textbook = str(textbook.get())
    inserted_how_teach = str(how_teach.get())
    inserted_attendance_check = str(attendance_check.get())
    inserted_english_lesson = str(english_lesson.get())
    inserted_lecture_style = str(lecture_style.get())

    sql = "insert into 상세강의스타일(강의스타일_교수_교수번호, 강의스타일_강의_교과번호, 평가_학생_학번, 교재, 강의방법, 출석체크, 원어, 강의스타일) values ('{}', " \
          "'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(prof_no, lec_no, inserted_student_id, inserted_textbook, inserted_how_teach, inserted_attendance_check,inserted_english_lesson,inserted_lecture_style)
    cur.execute(sql)

    conn.commit()
#교수님 정보 호출 함수
def show_professor() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()

    sql = "select * from 교수"
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 성함 : " + str(row[1]) + ", 소속학과 : " + str(row[2]) + ", 전화번호 : " + str(
            row[3]) + ", 연구실 위치 : " + str(row[4]) + ", 이메일 주소 : " + str(row[5]))
        row = cur.fetchone()
    print()
    conn.close()

#강의 호출 함수
def show_lecture():
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()

    sql = "select * from 강의"
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교과번호 : " + str(row[0]) + ", 강의 이름 : " + str(row[1]) + ", 강의 시간 : " + str(row[2]) + ", 인원 : " + str(
            row[3]) + ", 학점 : " + str(row[4]))
        row = cur.fetchone()
    print()
    conn.close()

#평가 테이블 만드는 함수('평가' 버튼 눌렸을 때)
def if_you_want_to_evaluate() :
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()

    lec_no = str(lecture_number.get())
    inserted_student_id = str(student_id.get())

    sql = "insert into 평가 values('{}', '{}')".format(lec_no, inserted_student_id)
    cur.execute(sql)

    conn.commit()

#교수님과 강의를 이은 강의 목록 호출하는 함수
def showdata_professor_and_lecture():
    conn = pymysql.connect(host='localhost', user='root', password='753951'
                           , db='termproject', charset='utf8')
    cur = conn.cursor()

    sql = "select * from 목록"
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print("교수번호 : " + str(row[0]) + ", 성함 : " + str(row[2]) + ", 교과번호 : " + str(row[1]) + ", 강의이름 : " + str(
            row[3]))
        row = cur.fetchone()
    print()
    conn.close()

window = Tk()
window.geometry("1500x1500")
window.title("강의 평가")
#레이블
#조회 레이블
Label(window, text = "조회").grid(column = 1, row = 0)
Label(window, text = "교과(강의) 번호: ").grid(column = 0, row = 1)
Label(window, text = "교수 번호: ").grid(column = 0, row = 2)
#입력 레이블
Label(window, text = "입력은 오른쪽을 이용해주세요").grid(column = 5, row = 3)
Label(window, text = "입력").grid(column = 7, row = 0)
#학생정보 입력 레이블
Label(window, text = "학번 : ").grid(column = 6, row = 1)
Label(window, text = "소속학과 : ").grid(column = 6, row = 2)
Label(window, text = "이름 : ").grid(column = 6, row = 3)
#시험성적 레이블
Label(window, text = "<시험성적>").grid(column =7, row = 4)
Label(window, text = "플러스 여부 : ").grid(column =6, row = 5)
Label(window, text = "시험 출제 스타일 : ").grid(column =6, row = 6)
Label(window, text = "퀴즈 여부 : ").grid(column =6, row = 7)
#과제 레이블
Label(window, text = "<과제>").grid(column =7, row = 10)
Label(window, text = "텀 프로젝트 : ").grid(column =6, row =11)
Label(window, text = "개인 과제 : ").grid(column =6, row = 12)
#특징 레이블
Label(window, text = "<특징>").grid(column =7, row = 13)
Label(window, text = "말 빠르기 : ").grid(column =6, row =14)
Label(window, text = "목소리 크기 : ").grid(column =6, row = 15)
Label(window, text = "이해 정도 확인 여부 : ").grid(column =6, row = 16)
Label(window, text = "강의 시간 초과 여부 : ").grid(column =6, row = 17)
Label(window, text = "강의력 : ").grid(column =6, row = 18)
#강의스타일 레이블
Label(window, text = "<강의스타일>").grid(column =7, row = 19)
Label(window, text = "교재 : ").grid(column =6, row =20)
Label(window, text = "강의 방법 : ").grid(column =6, row = 21)
Label(window, text = "출석체크 : ").grid(column =6, row = 22)
Label(window, text = "원어 : ").grid(column =6, row = 23)
Label(window, text = "강의스타일 : ").grid(column =6, row = 24)
#교수,강의, 목록 레이블
Label(window, text = "교수님 목록").grid(column =1, row = 6)
Label(window, text = "강의 목록").grid(column =1, row = 7)
Label(window, text = "교수님-강의 목록").grid(column =1, row = 8)
#입력 텍스트 레이블
Label(window, text = "평가를 위해서 학생정보 입력 버튼을 누르고 ").grid(column =9, row = 2)
Label(window, text = "교과번호와 학번을 필수적으로 넣고 왼쪽의 '평가' 버튼을 눌러주세요 ").grid(column =9, row = 3)

#엔트리
#교수번호, 교과번호 조회 엔트리
lecture_number = Entry(window, width = 20)
lecture_number.grid(column = 1, row = 1)
professor_number = Entry(window, width = 20)
professor_number.grid(column = 1, row = 2)
#학생 정보 입력 엔트리
student_id = Entry(window, width = 20)
student_id.grid(column = 7, row = 1)
student_major = Entry(window, width = 20)
student_major.grid(column = 7, row = 2)
student_name = Entry(window, width = 20)
student_name.grid(column = 7, row = 3)
#시험성적입력 엔트리
plus_or_not = Entry(window, width = 20)
plus_or_not.grid(column = 7, row = 5)
test_style = Entry(window, width = 20)
test_style.grid(column = 7, row = 6)
quiz_or_not = Entry(window, width = 20)
quiz_or_not.grid(column = 7, row = 7)
#과제입력 엔트리
term_project = Entry(window, width = 20)
term_project.grid(column = 7, row = 11)
private_assignment = Entry(window, width = 20)
private_assignment.grid(column = 7, row = 12)
#특징입력 엔트리
speaking_rate = Entry(window, width = 20)
speaking_rate.grid(column =7, row =14)
voice = Entry(window, width = 20)
voice.grid(column =7, row =15)
check_understanding = Entry(window, width = 20)
check_understanding.grid(column =7, row =16)
lecture_time = Entry(window, width = 20)
lecture_time.grid(column =7, row =17)
teaching = Entry(window, width = 20)
teaching.grid(column =7, row =18)
#강의스타일입력 엔트리
textbook = Entry(window, width = 20)
textbook.grid(column =7, row =20)
how_teach = Entry(window, width = 20)
how_teach.grid(column =7, row =21)
attendance_check = Entry(window, width = 20)
attendance_check.grid(column =7, row =22)
english_lesson = Entry(window, width = 20)
english_lesson.grid(column =7, row =23)
lecture_style = Entry(window, width = 20)
lecture_style.grid(column =7, row =24)
#버튼
btn_characteristic = Button(window, text = "특징", command = showdata_characteristic)
btn_characteristic.grid(column=3,row=3)
btn_assignmnet = Button(window, text = "과제", command = showdata_assignmnet)
btn_assignmnet.grid(column=3,row=2)
btn_test = Button(window, text = "시험", command = showdata_test)
btn_test.grid(column=3,row=1)
btn_style = Button(window, text = "스타일", command = showdata_style)
btn_style.grid(column=3,row=4)
btn_insert_test = Button(window, text = "시험성적입력", command = insert_test).grid(column = 8, row = 7)
btn_student_information = Button(window, text = "학생정보입력", command = insert_student_information).grid(column = 8, row = 3)
btn_insert_assignment = Button(window, text = "과제정보입력", command = insert_assignment).grid(column = 8, row = 12)
btn_insert_characteristic = Button(window, text = "특징정보입력", command = insert_characteristic).grid(column = 8, row = 18)
btn_insert_style = Button(window, text = "스타일정보입력", command = insert_style).grid(column = 8, row = 24)
btn_show_professor = Button(window, text = "교수", command =  show_professor).grid(column = 3, row = 6)
btn_show_lecture = Button(window, text = "강의", command =  show_lecture).grid(column = 3, row = 7)
btn_evaluate = Button(window, text = "평가", command = if_you_want_to_evaluate).grid(column = 8, row = 2)
btn_show_professor_and_lecture = Button(window, text = "교수님-강의", command =  showdata_professor_and_lecture).grid(column = 3, row = 8)

window.mainloop()