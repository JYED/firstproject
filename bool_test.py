# or연산의 결과는 앞의 값이 True이면 앞의 값을, 앞의 값이 False이면 뒤의 값을 따른다.

# 아무것도 안넣었으면 value = '아무것도 못받았어'
# 무언갈 입력 받았으면 value = '입력받은 값'
value = input('입력해 주세요 >') or '아무것도 못받았어'
print('입력받은 값 >',value)