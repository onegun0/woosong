#HWpython14_04_W3SetEx01_김선웅


#Set items are unchangeable
#you can remove items and add new items.


myset = {"apple", "banana", "cherry"}
print(myset)

#연습01(unordered)
thisset={"apple", "banana", "cherry","apple"}
print(thisset)

#연습02(len())
thisset={"apple","banana","cherry"}
print(len(thisset))

#연습03(any data type01)
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#연습04(any data type02)
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#연습05(type)
myset = {"apple", "banana", "cherry"}
print(type(myset))

#연습06
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)