#HWpython10_02_ListW3Chk04_김선웅

#연습01(end:append()) 뒤에 추가
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#연습02(specified index:insert()) 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#연습03(list:extend())
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#연습04(Any Collection Type 추가 가능)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
