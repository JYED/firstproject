my_list = [1,2,3,4,5,6]
print(my_list[0],my_list[1])

str = "Hello world"
print(str[0],str[1])

print ( 3 in my_list)
print ( 8 in my_list)
print ('H' in str)
print ('z' in str)
print(my_list.index(5))
print(str.index('r'))

characters = list('abcedf')
print(characters)
words = "Hello World는 프로그래밍을 배우기에 아주 좋은 사이트입니다."
words_list = words.split()      # 문장을 split시켜준다.
print(words_list)

time_str = "10:35:27"
time_list = time_str.split(":")
print(time_list)

print(":".join(time_list))             # 다시 합치기 (( time_list 자체는 바뀌지 않음))
print(" ".join(words_list))

"""
str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split()


# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장하세요.
position = words.index("흐림")


words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요. 
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)


print(new_str)
"""