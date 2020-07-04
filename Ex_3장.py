'''
x = int(input("첫 번째 수를 입력하시오:"))
y = int(input("두 번째 수를 입력하시오:"))
z = int(input("세 번째 수를 입력하시요:"))

avg = (x+y+z)/3

print("평균=",avg)
'''
'''
#1. 두개의 정수를 받아 다음을 출력
x = int(input("첫번째 정수를 입력하시오:"))
y = int(input("두번째 정수를 입력하시오:"))

합 = x + y
차 = x - y
곱 = x*y
평균 = (x+y)/2
큰수 = max(x,y)
작은수 = min(x,y)

print("두수의 합:",합)
print("두수의 차:",차)
print("두수의 평균:",평균)
print("두수의 곱:",곱)
print("두수의 큰수:",큰수)
print("두수의 작은수:",작은수)
'''
'''
#2. 원기둥의 부피를 계산하는 프로그램 작성
r = int(input("반지름을 입력하시오:"))
h = int(input("높이를 입력하시오:"))

vol = 3.141592*r**2*h

print("원기둥의 부피=",vol)
'''
'''
#3. 정수를 받아서 자리수별로 합을 계산
no = int(input("정수를 입력하시오:"))

no1 = no % 10

no10 = no //10
no10 = no10 % 10

no100 = no//100
no100 = no100 % 10

no1000 = no//1000
no1000 = no1000 % 10

no10000 = no//10000
no10000 = no10000 % 10

합 = no1 + no10 + no100 +no1000 + no10000
print("자리수의 합:",합)
'''
'''
#4. 두점의 좌표를 받아서 두점사이의 거리를 계산하는 프로그램
x1 = int(input("x1값을 입력하시오:"))
y1 = int(input("y1값을 입력하시오:"))
x2 = int(input("x2값을 입력하시오:"))
y2 = int(input("y2값을 입력하시오:"))

dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

print("두좌표간의 거리=",dist)
'''
'''
#5. 터틀그래픽
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.setheading(0) #???
t.left(45)
t.forward(141)
t.setheading(0)
t.forward(100)
t.left(90)
t.forward(100)
'''
'''
#7. time()호출ㅎ여 1970년 1월 1일 이후 흘러온 전체 초가 반환된다. 나누거나 나머지를 구해서 현재 시간의 시와 분을 계산할 수 있을까?
import time

fseconds = time.time()
'''
'''
#8. 움직이는 물체의 운동에너지 계산
weight = int(input("물체의 무게를 입력하시오(킬로그램):"))
speed = int(input("물체의 속도를 입력하시오(미터/초):"))

jul = 1/2*weight*speed**2           #??

print("물체는", jul,"(줄)의 에너지를 가지고 있다.")
'''

print("안녕하세요.")
name=input("이름이 어떻게 되시나요?")
print("만나서 반갑습니다.",name,"씨")
length=input("이름의 길이는 다음과 같군요:")
age=input("나이가 어떻게 되시나요?")
print("내년이며",age,"이 되시는군요.")
















