'''
#4장 연습문제
#3. 입력한 문자열 처음 2글자와 마지막2글자 추출 및 합쳐 출력
s=input("문자열을 입력하시오:")
print(s[:2]+s[-2:])
'''
'''
#4. 입력한 문자열 뒤에 항상 '하는중'을 붙이기
s=input("문자열을 입력하시오:")

print(s +"하는중")
'''
'''
#5. 입력한 기호(문자2개)안에 문자열을 삽입(???)

s1=input("문자열을 입력하시오:")
s2=input("문자열을 입력하시오:")
s3=input("중간에 삽입할 문자를 입력하시오:")

print(s1+s3+s2)
'''
'''
#6. 리스트 안의 숫자들을 꺼내서 합계를 계산하여 출력하는 프로그램을 작성
nlist = [1,2,3,4]
#n_sum = (nlist[0]+nlist[1]+nlist[2]+nlist[3])
n_sum=sum(nlist)
print("리스트 숫자들의 합 = ",n_sum)
'''

'''
#7. 입력한 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그 색상으로 채워진 원
color_list=[]
x1 = input("색상#1을 입력하시오:")
color_list.append(x1)
x2 = input("색상#2을 입력하시오:")
color_list.append(x2)
x3 = input("색상#3을 입력하시오:")
color_list.append(x3)
print(color_list)

import turtle   #???
t = turtle.Turtle()
t.shape("turtle")

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t. forward(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()
'''

'''
#########################################################chapter 5
#성적을 입력받아서 합격여부 판단
score = int(input("성적을 입력하시오:"))
if score >= 60:
    print("합격입니다")
else:
    print("불합격입니다")
'''
'''
#영화 나이 제한 검사
#1. 나이를 입력받는다 2. 15세 이상은 영화시청가능. 3. 15세 이하는 영화시청 불가능
age = int(input("나이를 입력하시오:"))
if age >= 15:
    print("당신은 이 영화를 볼 수 있습니다")
else:
    print("당신은 이 영화를 볼 수 없습니다")
'''
'''
# 윤년판단
year = int(input("연도를 입력하시오:"))

if ((year % 4 == 0) and (year % 100 !=0)) or (year % 400 == 0):
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")
'''

'''
#동전던지기 게임
#1. 난수생성
#2. 동전던지기
#3. 0이 나오면 앞면 1이 나오면 뒷면
#4. 게임 종료

import random

print("동전던지기 게임을 시작합니다.")
coin=random.randrange(1,7)#1~7 [1:7]

if coin == 1 :
    print("1입니다.")
elif coin == 2:
    print("2입니다.")
elif coin == 3:
    print("3입니다.")
elif coin == 4:
    print("4입니다.")
elif coin == 5:
    print("5입니다.")
else:#0
    print("6입니다.")

print(coin,"입니다.")
print("게임이 끝났습니다.")
'''
'''
# 종달새 문제
#1. 시간을 랜덤하게 선택
#2. 날씨는 좋다 나쁘다로 랜덤하게 선택
#3. 시간과 날씨에 대해 출력
#3. 종달새가 노래하는 조건을 줄것(시간, 날씨)
#4. 종달새가 노래를 할것인지 말것인지 출력

import random
time = random.randrange(1, 25)
sunny = random.choice([True, False])
print("좋은 아침입니다. 지금 시각은"+str(time)+"시 입니다.")

if sunny == True:
    print("현재 날씨가 화창합니다.")
else :
    print("현재 날씨가 화창하지 않습니다.")

if 6<=time <= 9 and sunny == True:
    print("종달새가 노래를 한다.")
else :
    print("종달새가 노래를 하지 않는다.")
'''
'''
num = int(input("정수를 입력하시오:"))
if num >= 0:
    if num == 0:
        print("0입니다.")
    else :
        print("양수입니다.")
else:
    print("음수입니다.")
    
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")
'''
'''
#사용자로부터 아이디를 받아 프로그램에 저장된 아이디와 일치하느지 여부를 출력하는 프로그램
id = "ILOVEPYTHON"
s = input("아이디를 입력하세요:")
if s == id:
    print("환영합니다.")
else :
    print("아이디가 다릅니다.")

pw = "kim181004"
t = input("패스워드를 입력하세요:")
if t == pw:
    print("환영합니다.")
else :
    print("패스워드가 틀립니다.")
'''
'''
#연습문제
#3. 현재온도를 질문하고, 25도이상이면 반바지 추천, 25도 미만이며 긴바지 추천
temp = int(input("현재온도를 입력하시오:"))
if temp == 25 :#필수
    pass
elif temp < 25 :#선택
    print("긴바지를 입으세요.")
else :#선택
    print("반바지를 입으세요.")
'''

#4. 시험점수를 물어보고 시험 점수가 90점 이상A

