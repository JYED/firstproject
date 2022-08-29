list = [1,2,3]
dict = {'one':1, 'two':2}

# 값 확인
print(2 in list)
print('two' in dict.keys())

#전부 삭제
list.clear()
dict.clear()

"""
list는 삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다.
Dict는 key로 값을 가져오기 때문에 삭제 여부와 상관이 없다.

list의 결합 : list1+list2
dict의 결합 : dict1.update(dict2)

dict1 = (1:100, 2:200)
dict2 = (1:1000, 2: 200, 3: 300)
dict1.update(dict2)
dict1

"""

dict1 = {1:100, 2:200}
dict2 = {1:1000, 2: 200, 3: 300}
dict1.update(dict2)
print(dict1)

dict1 = {1:100, 2:200}
dict2 = {1:1000, 2: 200, 3: 300}
dict2.update(dict1)
print(dict2)
print('\n\n')

##################
##################
##################
def check_and_clear(box):
    if '불량품' in box.keys():
        box.clear()
        print("불량품입니다")
    else:
        print("정상품입니다")

box1 = {"불량품" : 10}
check_and_clear(box1)
# {}가 출력되어야합니다.
print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
# {"정상품": 10}가 출력되어야합니다.
print(box2)