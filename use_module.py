#같은 폴더에 들어있어야한다 ( my_module.py와 use_module.py가)

import my_module

selected = my_module.random_rsp()
print(selected)
print('가위?', my_module.SCISSOR == selected)

