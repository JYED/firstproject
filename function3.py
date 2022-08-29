a = 1
b = 2
c = -8

def print_root():
    r1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1,r2))

def print_round(number):        #반올림하는 함수
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.6)