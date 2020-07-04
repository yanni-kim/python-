weight = float(input("몸무게를 kg 단위로 입력하시요:"))
height = float(input("키를 미터 단위로 입력하시요:"))

bmi = (weight/(height**2))*100
print("당신의 BMI=", bmi)
