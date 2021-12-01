#HWpython04_12_forEx03BreakContinue_김선웅

fruits=["apple", "banana", "cherry"]
for x in fruits:
	if x =="banana":
		continue
	print(x)

fruits=["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x =="banana":
		break
	
	