'''
message="철수가 '안녕'이라고 말했습니다."
print(message)

x=input("정수를 입력하시오:")
y=input("정수를 입력하시오:")
print(x+y)
'''
'''
friend_list = []

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오:")
friend_list.append(friend)

print(friend_list)
'''
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list=["yellow","red","blue","green"]

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()
'''

#3-7
#시간을 가져와서, 시,분,초

import time

t = time.time()#지금시간(초),영국시간대, #1970,1,1~#객체

sec=t%60 #0~59
r=t-sec #100만-sec
min_=r%(3600) #0~59
r=r-min_*60
hour=hour%(60*60*24)

#1,60,60,3600(60*60),24

'''
#list1

#사용자로부터 값을 3개의 이름을 받아서, 리스트에 저장하고,
#그 저장된 값을 순서대로 출력해주세요

#1. 리스트를 만든다
#2. 사용자로부터 이름을 입력받는다
#3. 3개의 이름을 받은후 리스트에 저장하고 그 값을 출력

name_list = [ ] #list
x = input("이름을 입력하세요:")#str
name_list.append(x)

x = input("이름을 입력하세요:")#str
name_list.append(x)

x = input("이름을 입력하세요:")#str
name_list.append(x)

print(name_list[2,1,0])

print(name_list[2],name_list[1],name_list[0])

print(name_list[::-1])
'''
'''
#x= int(input())
x=21
if x<=20:
    print("True")
elif x<30:
    print("middle")
else:
    print("False")


if True:
    if:
'''
'''
#5-7블록
#조건이 참인 경우에 여러 개의 문장이 실행되어야 한다면 어떻게 하나?
#15세이상 관람 가능

age=int(input("나이를 입력하세요:"))
if age>=15:
    print("이영화를 볼수 있습니다")
else:
    print("이영화를 볼수 없습니다.")
'''



















