#HWpython14_05_W3SetEx02_김선웅

#연습01(for in)
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#연습02(in)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


#Add Items
#연습01(Add_항목)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#연습02(set_update())
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#연습03(collection_update()) 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Item
#연습01(remove()_ErrorChk)
thisset = {"apple", "banana", "cherry"}
#thisset.remove("orange") 없는 걸 넣으면 에러
thisset.remove("banana")
print(thisset)

#연습02(discard_ErrorChk)
thisset = {"apple", "banana", "cherry"}
thisset.discard("orange") #없는 걸 넣어도 에러 안남 아무일도 일어나지 않음
print(thisset)

#연습03(pop())
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #값을 반환
print(thisset)

#연습04(clear())
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#연습05(del)
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)