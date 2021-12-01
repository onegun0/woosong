#HWpython03_05_option01_김선웅



i=int(input("반복하고자 하는 숫자를 입력해주세요:"))
star=1
'''
while True:
	print(" "*(i-1)+"*"*star)#end=) print("*"*star)

	
	if i==0:
		break
	i-=1
	star+=1
print(star)	
'''
while i>0:
	print("  "*(i-1), end="")
	print("☆"*star)
	if i==0:
		break
	i-=1
	star+=1

	