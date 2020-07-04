# x=10

# for i in range(x):#10번만큼 #횟수반복?
#     print(x)#10
    
# while x>10:#조건반복문

# # 주석 ctrl + /
# # 전체주석 - 범위 설정 ''''''

# for index in range(8):

# #range(start=0,stop,step=1) # 1 2 3
# print(list(range(6))) #[0, 1, 2, 3, 4, 5]
# # print(list(range(1,6))) #[1, 2, 3, 4, 5]
# print(list(range(1,10))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1,10,2))) #[1, 3, 5, 7, 9]

# for i in range(1,8,2):#0~7
#     print(10)

'''
#5장 본문
#난수를 이용하여 간단한 축구 게임을 작성. 사용자가 컴퓨터를 상대로 페널티 킥을 하고 3개의 영역중 하나를 수비
#1. 난수설정
#2. 어디를 수비할것인지 결정
#3. 컴퓨터 랜덤 선택과 나의 수비지역이 맞으면 성공
#4. 그렇지 않으면 패널티킥이 성공
import random

options=["왼쪽","중앙","오른쪽","왼쪽 상단","왼쪽하단","오른쪽상단","오른쪽 하단"]
computer_choice = random.choice(options)    #옵션을 랜덤으로 하여 변수로 설정
user_choice = input("어디를 수비하시겠어요?(왼쪽, 오른쪽, 중앙, 왼쪽상단, 외쪽하단, 오른쪽상단, 오른쪽 하단)")
if computer_choice == user_choice:
    print("수비에 성공하셨습니다.")
else:
    print("패널티킥이 성공하였습니다.")
'''
'''
#연습문제
#4. 시험점수를 물어보고 90점이상이면 A, 80점이상 B, 70점 이상 C, 60점 이상 D, 그외 F의 프로그램
score=int(input("시험점수는 몇점입니까?"))

if score >= 90 :
    print("성적은 A학점입니다.")
elif score >= 80 :
    print("성적은 B학점입니다.")
elif score >= 70 :
    print("성적은 c학점입니다.")
elif score >= 60:
    print("성적은 D학점입니다.")
else:
    print("성적은 F학점입니다.")    
'''
'''
#5. 난수를 사용, 1~100의 숫자를 생성, 뺄셈문제를 생성하고 사용자에게 답이 맞는지 검사하는 프로그램
import random
x = random.randint(1, 100)
y = random.randint(1, 100)
cal = x - y
print(int(cal))

ans = int(input("답은 무엇인가요?"))

if ans == cal :
    print("맞습니다.")
else :
    print("틀립니다.")
'''
'''
#6. 정수를 받아 2와 3으로 나누어 떨어질 수 있는지를 출력
n=int(input("정수를 입력하시오:"))

if n % 2 ==0 and n%3 ==0:
    print("2와 3으로 나누어 떨어집니다.")
'''



# #????7번. 사용자가 가지고 있는 복권번호가 2자리 모두 일치하면 100만원, 하나만 일치하면 50만원, 하나도 일치하지 않으면 상금없음. 복권번호 난수, 상금출력
# #1. 사용자 2자리 복권번호 받기
# #2. 복권번호 난수로 생성
# #3. 두자리중 맞는 수에 따른 상금 제시 (상금은 00원입니다)

# lotto=int(input("2자리 복권번호 digit1과 digit2를 입력하시오:"))#64

# lotto_digit1 = lotto // 10 #0~9,몫 , 십의자리,앞자리,6
# lotto_digit2 = lotto % 10 #0~9,나머지, 1의자리,4

# import random

# n = random.randint(1,99) #랜덤값
# # n = 98

# n_digit1 = n // 10 #0~9,몫 , 십의자리 #9
# n_digit2 = n % 10 #0~9,나머지, 1의자리 #8

# if lotto==n:
#     # print("상금은"+100+"만원입니다")
#     print(f"상금은 {100}만원입니다")#f-string
# elif lotto_digit1==n_digit1 or lotto_digit2 == n_digit2:
#     print(f"상금은 {50}만원입니다")
# else:
#     print("상금은 없습니다")


# a, b = map(int,input("두 정수 a,b를 입력하시오:").split())
# print(a*b)
print("a")


'''
a,b=input("두 정수 a,b를 입력하시오:").split()
a=int(a)
b=int(b)
print(a+b)


a,b,c=input("세 정수 a,b,c를 입력하시오:").split()
a=int(a)
b=int(b)
c=int(c)
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
'''
'''
# 백준:사분면 구하기
x=int(input("x좌표의 정수를 입력하시오:"))
y=int(input("y좌표의 정수를 일별하시오:"))

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)
'''
'''
#알람일찍설정하기
H,M = input("시와 분을 입력하시오:").split()
print(H,"시",M,"분")

if (M-45)<=0:
'''    

