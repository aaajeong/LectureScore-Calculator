# PythonLecture 클래스 정의
# <멤버변수>
# 1차 시험점수 - First_g
# 2차 시험점수 - Second_g
# 3차 시험점수 - Third_g
# 결석횟수 - abs_num
#
# <멤버함수>
# 3개 시험의 평균 점수 산출 함수 - exam_avg
# 3개의 점수를 20%, 30%, 50% 가중치로 평균 산출 함수 - weighted_avg
# 최종 성적을 입력받아 학점을 부여하는 함수 - get_Alphabet
# * 초기화 함수에서 각 점수들이 0 점으로 초기화 되도록.


class PythonLecture:
    def __init__(self, First_g = 0, Second_g = 0, Third_g = 0, abs_num=0,):
        self.First_g = First_g
        self.Second_g = Second_g
        self.Third_g = Third_g
        self.abs_num = abs_num
    def exam_avg(self):
        sum = self.First_g + self.Second_g + self.Third_g
        result = sum/3
        return result
    def weighted_avg(self):
        result = self.First_g*0.2 + self.Second_g*0.3 + self.Third_g*0.5
        return result
    def get_Alphabet(self, grade, abs_num):
        self.grade = grade
        self.abs_num = abs_num

        if(abs_num>=5):
            return "F"
        elif grade>=90 and grade<=100:
            return "A"
        elif grade>=80 and grade<90:
            return "B"
        elif grade>=70 and grade<80:
            return "C"
        elif grade>=60 and grade<70:
            return "D"
        elif grade<60:
            return "E"




