
#list의 변경
#list[5]=6          => error
list = [1,2,3,4,5]
print(list[2])
list[2]=33
print(list[2])


#list의 추가
list.append(6)

print(list)

dict = {
    'one' : 1,
    'two' : 2
}

#dict의 추가
print(dict)
dict['three'] = 3
print(dict)

#dict의 변경
dict['one'] = 11
print(dict)

#list의 삭제
del(list[0])
print(list)
list.remove(5)
print(list)
list.remove(list[0])
print(list)

#dict의 삭제
#dict.remove('one')     => error
del(dict['one'])
print(dict)

# pop은 값을 반환하면서 삭제한다.
print(dict.pop('two'))
print(dict)