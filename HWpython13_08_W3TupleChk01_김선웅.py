#HWpython13_08_W3TupleChk01_김선웅
#연습1(round brackets)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#연습2(Duplicates)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#연습3(len())
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
	
#연습4(create Tuple With One Item)			
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))			

#연습5(type01)		
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

#연습6(type02)
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))

#연습7(Constructor_double round-brackets)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)