# 범위 내의 데이터중 선택해서 가져오고 싶은 경우

list1 = list(range(20))
print(list1)

print(list1[5:15])
print(list1[5:15:2])    # 2개마다 출력
print(list1[5:15:3])    # 3개마다 출력
print(list1[15:5:-1])   # 1씩 내려가면서 출력 
print(list1[14:4:-1])
# print(list1[5:15:-1])    error. 이유는 5에서 -1씩 하면 15를 만날 수 없기 때문.
print(list1[::3])
print(list1[::-3])