a = 10
if a<10 and 2**a > 1000 and a%5 == 2 and round(a) == a:
    print("복잡한 식")

#################
def return_false():
    print("함수 return_False")
    return False

def return_true():
    print("함수 return_true")
    return True

print("테스트1")
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)

##################

if return_false() and return_true():  #첫번째 값인 return_fasle()에서 이미 False이므로
                            # 뒤에 return_true()는 쳐다보지도 않는다. 이를 단락평가라고함
    print("True")
else:
    print("False")

###################
dic = {"key2" : "value1"}

if "key1" in dic and dic["key1"] == "value1": #단락평가가 없으면 key1이 없으므로 에러발생
    print("key1도 있고, 그 값은 value이다.")
else:
    print("아니네")