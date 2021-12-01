#HWpython02_07_IFpractice03_김선웅

'''
조건
사용자 점수 입력
90점 이상이면: a
80점 이상이면: b
70점 이상이면: c
'''
score= input("점수를 입력하세요:")
vscore=score

if vscore >=int(90):
	print("A학점")
elif int(90)>vscore>=int(80):
	print("B학점")
elif int(80)>vscore>=int(70):
	print("C학점")