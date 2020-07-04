'''
street = input("주소는 어디 인가요?:")
type = input("거주형태는 어떻게 되나요?:")
size = int(input("방 수는 어떻게 되나요?:"))
price = int(input("가격은 어떻게 되나요?:"))

print("################################################")
print("#"*30)
print("#"+" "*28+"#")
print("#                                              #")
print("#             부동산 매물 광고                 #")
print("#                                              #")
print("################################################")
print(street,"에 위치한 아주 좋은", type,"가 매물로 나왔습니다. 이", type,"는", size,"개의 방을 가지고 있으며 가격은", price,"원 입니다.")
print("좋은", type,"를 놓치지 마십시요.")
'''
'''
name = input("이름을 입력하세요:")
age = input("나이를 입력하세요:")
year = input("연도를 입력하세요:")
xyear = int(year) - 2020
cal = int(xyear) + int(age)
print(name,"씨는",year,"년에",cal,"살이시네요.")
'''

'''
#연습2. 3개의 숫자를 받아서 평균을 계산하고 결과를 출력하는 프로그램
x=input("첫번째 숫자를 입력하세요:")
y=input("두번째 숫자를 입력하세요:")
z=input("세번째 숫자를 입력하세요:")
avg = (int(x)+int(y)+int(z))/3
print(x,y,z,"의 평균은",avg,"입니다.")
'''
'''
import math #모듈

#연습3. 사용자로부터 원의 반지름을 입력받아서 원의 변적을 계산
r=input("반지름을 입력하시요:")
area = (int(r)**2)*math.pi
print("반지름이",r,"인 원의 넓이:",area)

'''
'''
#연습4. radius변수를 20씩 증가시키면서 원 3개 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.down()
t.forward(100)#100
t.left()
t.right()
t.fd(-100)
t.lt()
t.rt()


t.goto(0,0)
t.circle(50)
t.goto(100,0)
t.circle(70)
t.goto(200,0)
t.circle(90)
'''

'''
p = int(input("분자를 입력하세요:"))
q = int(input("분모를 입력하세요:"))
print("나눗셈의 몫=", p//q)
print("나눗셈의 나머지=",p%q)

number = int(input("나눗셈의 나머지를 다시 입력하세요:"))
print(number%2)
'''
'''
sec=int(input("초를 입력하세요:"))
min=sec//60
remaider=sec%60
print(min,"분",remaider,"초")
'''

'''
#원하는 다각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리겠습니까?"))
for i in range(n):
    t.forward(50)
    t.left(360//n)  
'''

'''
#커피가게 매출 계산하기
amcano = int(input("아메리카노 판매 갯수 :"))
cost1 = amcano*2000
cate = int(input("카페라테 판매 갯수 :"))
cost2 = cate*3000
cachi = int(input("카푸치노 판매 갯수 :"))
cost3 = cachi*3500
cost = cost1 + cost2 + cost3
print("총 매출은",cost,"원 입니다.")
'''
'''
#화씨온도를 섭씨온도로 바꾸기
fhit = int(input("화씨온도를 입력하세요:"))
chit = (fhit-32)*5/9
print("섭씨온도는",chit,"도 입니다.")
'''
'''
#BMI 계산하기
weight = float(input("몸무게를 kg단위로 입력하세요:"))
height = float(input("키를 meter단위로 입력하세요:"))
bmi = weight/(height**2)
print("당신의 BMI는",bmi,"입니다.")
'''

#자동판매기 프로그램
money = int(input("투입한 돈:"))#7160
cost = int(input("물건값:"))#6000
change = money - cost#1160
print("잔액:",change)
coin500 = change//500#2
print("500원 동전 갯수:", coin500)
change1=change % 500#160
coin100 = change1//100#1
print("100원 동전 갯수:",coin100)
change2 = change1 - 100 #60
coin50=change2 // 50  #60%50
print("50원 동전 갯수:",coin50) #1
change3 = change2 - 50
coin10=change3//10  #1               
print("10원 동전 갯수:",coin10)















