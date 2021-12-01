#HWpython10_03_ListW3Chk05_김선웅

#연습01 (item삭제-값 반환 불가능)
thislist = ["apple", "banana", "cherry"]
result=thislist.remove("banana")
print(thislist)
print(result)
#연습02(index로 삭제- 값 반환 가능)
thislist = ["apple", "banana", "cherry"]
result=thislist.pop(1)
print(thislist)
print(result)

#연습03(기본은 뒤부터)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#연습04(삭제)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#연습05(구조도 삭제)
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)

#연습06(구조는 남겨두고 값만 삭제)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)