#HWpython09_10_ListW3Chk03_김선웅

#연습01(index number)
thislist=["apple", "banana", "cherry"]
thislist[1]="blackcurrant"
print(thislist)

#연습02(range01)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#연습03(range02)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#연습04(range03)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#연습05
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)