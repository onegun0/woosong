#HWpython13_08_W3TupleChk02_김선웅
#연습1(index)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#연습2(Negative)
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#연습3(Range01)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
	
#연습4(Range02)			
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
	

#연습5(Range03)		
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#연습6(Range04_Negative)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#연습7(in)
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")