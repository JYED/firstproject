#for i in [0,1,2,3,4, ... , 999, 1000]:
#   print(i)


# 0부터 10개의 숫자 출력
for i in range(5):
    print(i)

names = ['철수','영희','바둑이','귀도','비단뱀']
for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))

# enumerate는 인덱스넘버와 value를 동시에 출력하기때문에 변수 두개 필요!
for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))

for i in range(11172):
    print(chr(44032 + i), end=' ')