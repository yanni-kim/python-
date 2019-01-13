"""
age= 3
name = "yeonhee"
pie = 3.14
notYet = None
"""
userList = [1,2,3,4,5]   #배열. 똑같은 타입을 복수개로 저장할때
ages = [11,22,33,44,52]

print(ages[0]) #첫번째 요소 인덱싱


subAges = ages[1:2] #슬라이싱
print(subAges)

subAges = ages[1:3] 
print(subAges)

fromTwoToLast = ages[1:]
print(fromTwoToLast)
