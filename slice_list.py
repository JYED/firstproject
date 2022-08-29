numbers = list(range(10))
print(numbers)

del numbers[0] # 인덱스 0 위치의 값 삭제
print(numbers)

del numbers[:5] # 처음 ~ 인덱스 4까지 삭제
print(numbers)

print(numbers[1:3])
numbers[1:3] = [77,88] # 범위 변경. 꼭 같은 개수일 필요는 없다.
print(numbers)

numbers[1:3] = [10,11,12]
print(numbers)

numbers[1:3] = range(10)    
print(numbers)

numbers[1:11] = [2] 
print(numbers)