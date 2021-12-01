#HWpython06_02_multiForEx02GUGuDan_김선웅


alignCenter="{0:^10}".format("단")
print("="*130, "\n")
for dan in range(2,10):
	print(dan, alignCenter, end="\t")
print("\n")
print("="*130)

for y in range(2,10):
	for x in range(2,10):
		print(x,"X", y, "=", x*y, end="\t")
	print()


