# 기존에는 한가지만 가져올 수 있다.
list = [1,2,3,4,5]
print(list[1])

text = "hello world"
print(text[1])

# slicing은 범위단위로 가져올 수 있게 해준다.

print(text[1:5]) # index 1 부터 4까지 출력
print(text[2:len(text)]) # index 2 부터 text의 길이끝까지 출력
print(text[2:]) # index 2 부터 출력
print(text[:3]) # index 3 전 까지 출력
print(text[:])  # 처음부터 끝까지 출력 
                # => 원래 있던 리스트를 넘겨주는게 아닌
                #  똑같은 값을 가진 새로운 리스트를 만들어서 출력한다.