#HWpython03_08_WhileExstar02_김선웅

'''
숫자입력 받기
sample run
반복하고자 하는 숫자를 입력하세요:5
☆
☆☆
☆☆☆
☆☆☆☆
☆☆☆☆☆
'''

i=int(input("반복하고자 하는 숫자를 입력해주세요:"))
star=1
while True:
	print("☆"*star)

	if star==i:
		break
	star+=1

'''
i=int(input("반복하고자 하는 숫자를 입력해주세요"))
star=1
while i>0:
	print("☆"*star)
	star+=1
	i-=1
'''