'''class Calc:
    @staticmethod #데코레이터
    def add(a,b):
        print(a+b)
def hello():
    print("hello")

#1. hello 프로그램 만든다
# hello 출력
#2. 수정
#인사가 시작되었습니다.
#hello
#인사가 끝났습니다.
#3. hello 함수에 + 다른 꾸며주는거 추가하자.(인사가 시작됐습니다.)
#print("인사가끝났습니다")'''

'''def test(function): #데코레이터 생성을 위해 만들었음
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper()
@test
def hello():
    print("hello")
    #두개 함수 합치는 거 이거 데코레이션이라고 함'''

'''class Student: #클래스 선언 똑같은 기능 복제하기 위해서 쓴다.
    def __init__(self,name,korean, math, english, science): #생성자,최소한의 변수를,나 자신을 클래스 내부에서 쓰겠다 init self
        self.name = name #메모리에 저장해준다. #첫번째 매개변수로 self 입력해야함, 클래스 생성을 위해서 생성자는 언더바__init__써야된다.
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self): #메소드 선언
        return self.korean+self.english+self.math+self.science  #클래스 내부에서 쓰기 위해서 self를 생성함
        # 나 자신을 쓰기 위해서 내부 함수에 있는 메모리에 적재하고자 만들었슴
    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

    #def __del__(self): 이거 하면 메모리에서 삭제가 된다. 잘 안쓴다.
#클래스 안에 여러 함수들을 써넣음
#학생 선언
#student = Student() #클래스 붕어빵 틀 student 안에 Student라는 클래스를 복사해줌
#붕어빵

students = [ #학생 리스트 선언
    Student("ㅇㅇㅂ",12,34,23,45), #pass라는 코드만 있는 복사본
    Student("ㅇㅁㄴ",34,55,63,32),
    Student("ㅈㄹㅈ",23,56,78,66),
    Student("ㅇㅂㄷ",12,43,54,22),
    Student("ㄹㄷㄹ",53,25,29,38),
]

#student 클래스 만들고 0~4번으로 만들었음
students[0].science
#->이름 국어 영어 수학 과학 점수 들어있음, 접근 하기 위해서 접근 지정 연산자 . 을 써야한다.
students[1].name
#이름 접근, 안적으면 주소만 출력이 된다.
students[2].math
students[3].korean
students[4].english

print("이름","총점","평균",sep ="\t")
for student in students:
    print(student.to_string())
print(students[0].science)'''

'''def create_student(name,korean,math,english,science):
    return{"name":name, "korean":korean,"math":math, "english":english,"science":science}
def student_get_sum(studnet):
    return student["korean"]+student["math"]+\
        student["english"]+student["science"]
def student_get_average(student):
    return student_get_sum(student)/4
def student_to_string(student):
    return "{}\t{}\t{}".format( student["name"],student_get_sum(student),student_get_average(student))

students = [
    {"name":"이", "korean":87, "english":88, "science":95}
    {"name":"삼", "korean":89, "english":81, "science":93}
    {"name":"사", "korean":90, "english":89, "science":92}
    {"name":"오", "korean":91, "english":45, "science":91}
    {"name":"육", "korean":23, "english":32, "science":97}
            ]

print("이름", "총점","평균", sep ="\t")  #sep: 각각의 문자를 탭으로 띄우겠다
for student in students:
    print(student_to_string(student))'''

'''class Student:
    def study(self):
        print("공부를 합니다")
class Teacher:
    def teach(self):
        print("학생들을 가르칩니다.")
classroom = [Student(),Student(),Teacher(),Student(),Student()]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person,Teacher):
        person.teach()'''

'''students = Student()
print("isinstance(클래스 선언된 변수, 클래스 이름)", isinstance(students,Student)) #속해있는지 안해있는지만 판단하는 것'''

'''class Student: #클래스 선언 똑같은 기능 복제하기 위해서 쓴다.
    def __init__(self,name,korean, math, english, science): #생성자,최소한의 변수를,나 자신을 클래스 내부에서 쓰겠다 init self
        self.name = name #메모리에 저장해준다. #첫번째 매개변수로 self 입력해야함, 클래스 생성을 위해서 생성자는 언더바__init__써야된다.
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):  # 메소드 선언
        return self.korean + self.english + self.math + self.science  # 클래스 내부에서 쓰기 위해서 self를 생성함
        # 나 자신을 쓰기 위해서 내부 함수에 있는 메모리에 적재하고자 만들었슴
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self): #to string 명령어를 다시 정의 한 것 __str__string을 문자열 출력하는걸로 바꾸겠다.
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
    def __eq__(self, value):
        return self.get_sum() == value.get_sum() #두개 더하는 기능으로 == 을 바꾼다.'''

'''class Student:
    count = 0 #클래수 변수 초기화
    def __init__(self,math):
        self.math = math #인스턴스 변수
        Student.count += 1 #student에 속하는 count
        print("{}번".format(Student.count))

students = [Student(10),Student(20)]
print()
print("현재 생성된 총 학생수는{}명".format(Student.count))'''

#garbage 컬렉터
class Test:
    def __init__(self):
        self.name = name #메모리에 저장
    def __del__(self):

Test("a") #self.name, 메모리에 저장된다. 메모리에 a가 적재된다. del 키워드메모리가 비워진다. 소거된다. 가비지 컬렉터
Test("b")

b = Test("b") #소거 되기 전에 b공간에 저장된다.
#메모리에 스왑파일 만든다.