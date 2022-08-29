list1 = [135,462,27,2753,234]
print(list1.index(27))         # 특정 값의 인덱스값 반환

# print(list1.index(50))          # ValueError 발생

if 50 in list1:
    print(list1.index(50))

list2 = [1,2,3] + [4,5,6]
print(list2)
print(list1)
list1.extend([9,10,11])         # 덧셈을 사용하는것보다 성능이 낫다
print(list1)

list1.insert(2,999)             # 인덱스 2에 999를 넣는ㄷ다.
print(list1)

list1.insert(-1,9999)
print(list1)
#   print(list1[10000]) 인덱스를 넘겨서 에러.
list1.insert(10000,555) # insert를 할 땐 가능. 
print (list1)

list1.sort()
print (list1)
list1.reverse()
print (list1)

"""
def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)

    else:
        return 
None
"""