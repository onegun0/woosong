#HWpython02_07_IFpractice03_김선웅

'''
조건
사용자 점수 입력
90점 이상이면: a
80점 이상이면: b
70점 이상이면: c
'''

score= int(input("점수를 입력하세요:"))


if 100 >= score >= 90:
	print("A학점")
elif score >= 80:
	print("B학점")
elif 80 > score >=0:
	print("C학점")
else:
	print("점수를 100 이하로 다시 입력하세요")