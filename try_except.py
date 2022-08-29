text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요'.format(text))


def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:      # Exception으로 쓰거나 아무것도 쓰지 않아도 된다.
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

# if문으로도 해결할 수 있다. 상황에 따라 맞는걸 쓰는게 좋다. 
"""def safe_pop_print(list,index):
    if(index<len(list))
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))"""
    
