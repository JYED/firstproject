# 인사로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# old way
print(number, '번 손님', greeting, '.', place, '에 오신 것을','welcome', '!')

# new way 
base = '{}번 손님, {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome)

# old way와 new way 둘 다 편할때가 다르다. 알아서 쓰자

print(base)
print(new_way)

# {}수가 많아도 오류가 나지않을때도 있으니 주의해야한다.