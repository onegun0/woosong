#HWpython03_07_WhileExstar01_김선웅

'''
숫자입력 받기
sample run
반복하고자 하는 숫자를 입력하세요:5
☆☆☆☆☆
☆☆☆☆
☆☆☆
☆☆
☆
'''

i=int(input("반복하고자 하는 숫자를 입력해주세요:"))

while True:
	print("☆"*i)
	if i == 1:
		break
	i-=1

'''
while i:
	print("☆"*i)
	i-=1
'''