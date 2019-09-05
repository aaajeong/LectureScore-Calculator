from Cal import PythonLecture


print("="*26)
print("Python Lecture Score Calculator")
print("="*26)

#학생의 점수와 결석 횟수 입력
s1_Info = input("Student 1 > ")
s2_Info = input("Student 2 > ")
s3_Info = input("Student 3 > ")

#빈칸으로 구분된 각각의 점수와 결석 횟수를 저장.
s1_Score1, s1_Score2, s1_Score3, s1_absnum = s1_Info.split(" ")
s2_Score1, s2_Score2, s2_Score3, s2_absnum = s2_Info.split(" ")
s3_Score1, s3_Score2, s3_Score3, s3_absnum = s3_Info.split(" ")

print("{0:=^26}".format("Result"))

# PythonLecture 클래스 생성
W_Cal1 = PythonLecture(int(s1_Score1), int(s1_Score2), int(s1_Score3), int(s1_absnum))
W_Cal2 = PythonLecture(int(s2_Score1), int(s2_Score2), int(s2_Score3), int(s2_absnum))
W_Cal3 = PythonLecture(int(s3_Score1), int(s3_Score2), int(s3_Score3), int(s3_absnum))

#weighted_avg함수를 사용해서 가중치가 고려된 평균값을 구한다.
result1 = W_Cal1.weighted_avg()
result2 = W_Cal2.weighted_avg()
result3 = W_Cal3.weighted_avg()

#get_Alphabet함수를 사용해서 각 학생의 알파벳 점수를 구한다.
S1_alphaBet = W_Cal1.get_Alphabet(result1, int(s1_absnum))
S2_alphaBet = W_Cal2.get_Alphabet(result2, int(s2_absnum))
S3_alphaBet = W_Cal3.get_Alphabet(result3, int(s3_absnum))

print("Num  Score  Grade")
print("%2s %7.2f %4s" %(1, result1, S1_alphaBet))
print("%2s %7.2f %4s" %(2, result2, S2_alphaBet))
print("%2s %7.2f %4s" %(3, result3, S3_alphaBet))