"""list = [1,2,3,5,7,2,5,237,55]
for val in list:
    if val % 3 == 0:
        print(val)
        break
        #continue"""

numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue       
    print("{}을(를) {}로 나누면 {}".format(a, b, a/b))