selected = None


while selected not in ['가위','바위','보']:
  selected = input('가위, 바위, 보 중에 선택하세요 > ')

print('선택된 값은:',selected)

patterns = ['가위','보','보']
for pattern in patterns:
  print(pattern)

"""
pattern = "보"
while pattern in patterns:
  pattern=input('패턴 입력 >')
  print(pattern)
"""

for pattern in range(len(patterns)):
  print(patterns[pattern])

length = len(patterns)

w