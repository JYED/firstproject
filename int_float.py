five1 = 5
five2 = 5.0
five3 = 5.00000

print(five1)
print(five2)
print(five3)

five4 = five1 * 1
five5 = five2 * 1
five6 = five1 * 1.0
five7 = five2 * 1.0

fives = '1. {}\n2. {}\n3. {}\n4. {}\n'.format(five4,five5,five6,five7)
print(fives)

print(6/5)
print(10/5)

print(6%5)
print(10%5)

dive1 = 6 / 5
dive2 = 6 // 5
print('div1 = {}, dive2 = {}'.format(dive1,dive2))

#-----------------------

a = 6
b = 5
print(a==b * (a // b) + (a%b))
print(0.1+0.1 == 0.2) # true
print(0.1+0.1+0.1 == 0.3) # true?? 직관적인 결과와는 다를 수 있다
# 정확해야하지만 정수를 써도 괜찮을때와 정확하지않아도 실수를 써야할 때 로 구분
# 때에 따라 정수와 실수를 바꿔가면서 써야함 =>
print(int(5.0))
print(float(5))
print(5*1.0)