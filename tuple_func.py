list = [1,2,3,4,5]
for i,v, in enumerate(list):
  print('{}번째 값 : {}'.format(i,v))

print('\n')

for a in enumerate(list):
  print('{}번째 값 : {}'.format(a[0],a[1]))

print('\n')

# *는 튜플을 쪼개라는 의미
for a in enumerate(list):
  print('{}번째 값 : {}'.format(*a))

print('\n')
# dictionary인 경우

ages = {'Tod':35, 'Jane':23, 'Paul':62}

for key,val in ages.items():
  print('{}의 나이는:{}'.format(key,val))
print('\n')

for a in ages.items():
  print('{}의 나이는:{}'.format(a[0],a[1]))

print('\n')
for a in ages.items():
  print('{}의 나이는:{}'.format(*a))