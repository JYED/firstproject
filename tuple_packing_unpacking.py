# 튜플을 이용해서 하나의 변수에 여러개의 변수를 대입할 수 있다.
# 대입하는걸 packing 그 중 값을 뺴오는걸 unpacking이라고 한다.

# a와 b로 이어진 튜플, 1과 2로 이어진 튜플.
a,b = 1,2
print(a)
print(b)

c = (3,4)
print(c)

d,e = c # unpacking
print("d : {}".format(d))
print("e : {}".format(e))

f = d,e # packing
print(f)

# 일반적인 값 교환
x=5
y=10
temp = x
x=y
y=temp
print(x,y)
# packing, unpacking을 이용한 값 교환
x,y = y,x
print(x,y)