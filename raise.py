# 에러를 직접 발생시킨다.
"""
def rsp(mine,yours):
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if  yours not in allowed:
        raise ValueError

try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값 입력')
"""

try:
    school = {'1반':[172,185,198,177,165,199], '2반':[165,177,167,180,191]}
    for class_number, students in school.items():
        for student in students:
            if student>190:
                print(class_number,'반에 190 넘는 학생 존재')
                raise StopIteration
except StopIteration:
    print('정상종료')
    
"""
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for shop, products in shops.items():
    for product, price in products.items():
        if product =='풀':
            print("{}: {}원".format(shop, price))"""