import random

wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

messages = {
    'win':'이겼다!',
    'lose':'졌다!',
    'draw':'비겼다!'
}

def rsp(mine,yours):
    if mine == yours:
        return messages['draw']
    elif wintable[mine] == yours:
        return messages['win']
    else:
        return messages['lose']

result = rsp('가위','바위')
print('\n'+result+'\n')


table = {
    '이름':'값',
    '하나':1,
    '둘':2,
    '리스트':random.choice([1,2,3])
}


print(table['이름'])
print(table['하나'])
print(table['둘'])
print(table['리스트'])

# 값에 리스트가 올 수도 있다.