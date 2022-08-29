list1 = [1,2,3,4]
list1.append(5)
print(list1)
list1.remove(1)
print(list1)

# 순서가 정해진 값의 집합이지만 불변하길 원하면 tuple을 사용하면 됨
#
#tuple1 = (1,2,3)
#tuple2 = 1,2,3
#list3 = [1,2,3]
#tuple3 = tuple(list3)
#if tuple1 == tuple2 == tuple3:
#    print("tuple1과 tuple2와 tuple3은 모두 같습니다.")

dict1 = {1:"one", 2:"two"}
print(dict1)
print(type(dict1))

tuple1 = (1,2,3)


tuple1 = {1,2,3}

print(tuple1)
print(type(tuple1))

tuple2 = 1,2,3

print(tuple2)

print(type(tuple2))

list1 = [1,2,3]
tuple3 = tuple(list1)
print(tuple3)
print(type(tuple3))
print(tuple3[0])
print(tuple3[1])
# error : tuple3[0]=5, print(tuple3) => 튜플은 불변 del,pop도 불가

