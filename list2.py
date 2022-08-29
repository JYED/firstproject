list2 = [37,23,10,33,29,40]
print(list2)

#list2.append(16)
#print(list2)

list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)

# 값이 들어있는지 체크
n = 12
ownership = n in list3
print(ownership)

n = 10
if n in list3:
    print('{}은 있어!'.format(n))

# 삭제, delete 해당하는 위치의 값 삭제
print(list4)
del list4[12] #12번째 인덱스 삭제
print(list4)

# 같은 값이 여러개 있어도 가장 먼저 나오는 값 삭제
list4.remove(40)
print(list4)