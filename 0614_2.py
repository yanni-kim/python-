'''
a=10
b="문자"
c=True
d=10.5

print(a)#10
print("a")#a

str(a)#type str a


#오늘의 온도는 몇 도 입니까?
#오늘은 몇 도 입니다.

print("오늘의 날씨는 맑습니다.")
'''
'''
temp = int(input("오늘의 온도는 몇 도 입니까?"))#int
print("오늘은", temp, "도 입니다.")#part 3
print("오늘은 "+str(temp)+"도 입니다.")#part1
print(f"오늘은 {temp}도입니다")#f-spring


temp#변수 ="오늘" #값
"temp"#값(인수)
           
b="today"
c=10
print("c")#today
'''
'''
#두 값을 사용자로부터 받아서(input), 두 값을 곱하고 출력해주시고,
#2번) 두 값을 나눈 값을 출력해주세요

a = int(input("숫자를 입력하세요"))
b = int(input("두번째 숫자를 입력하세요"))

c= a*b
print(c)

print(a//b)

a = int(input())
'''
'''
#필수-문제
#투입금액을 받고, 물품을 구입 후,
#거스름돈을 500원,100원 으로 반환을 해주는 문제

#옵션-알고리즘
#사용자로부터 금액을 입력 받는다.

#구매할 가격을 입력받는다.

#입력받은 금액과 물품의 차액을 계산한다.
#남은 차액을 500원과 100원으로 계산한다.


cash = int(input("현금을 넣으세요")) #3000

buying_cash = int(input("구매할 가격을 입력하세요")) #2300

refund = cash-buying_cash #700

coin500 = refund//500 #1

charge = refund-(coin500*500) #700-(1*500)
#charge = refund%500 #700%500 -> 200

coin100 = charge//100

print("나머지는 500원", coin500,"개 이고","100원", coin100,"개 입니다")
'''
'''
refund = cash - buying_cash
coin500 = refund//500
charge = refund-(coin500*500)
coin100 = charge//100
'''

#제시된 변수를 사용하여 제시된 부동산 광고를 화면에 출력

street = "서울시 종로구"
shape = "아파트"
number_of_rooms = 3
price = 100000000

print("======================")
print("=  부동산 매물 광고  =")
print(street,"에 위치한 아주 좋은", shape, "가 매물로 나왔습니다. 이 아파트는", number_of_rooms, "개의 방을 가지고 있으며 가격은", price,"입니다.") 






