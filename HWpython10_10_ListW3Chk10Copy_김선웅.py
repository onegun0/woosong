#HWpython10_10_ListW3Chk10Copy_김선웅

result01=["apple", "banana", "cherry"]
result02=["apple", "banana", "cherry"]

print(result01)
print(result02)


result03=result01

print(id(result01))
print(id(result03))	#주소값 같음(result01참조)


result04=result01.copy()

print(id(result01))
print(id(result04))	#주소값 다름

result05=list(["apple", "banana", "cherry"])
result06=list(["apple", "banana", "cherry"])

print(id(result05))	#새로운 주소값 생성
print(id(result06))	#새로운 주소값 생성