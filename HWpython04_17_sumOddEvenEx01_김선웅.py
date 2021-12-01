#HWpython04_17_sumOddEvenEx01_김선웅

'''
1. 1~10까지 합을 출력 누적
2. 1~10까지의 홀수합을 출력
3. 1~10까지의 짝수합을 출력
'''

y=0
for x in range(1,11): #1,2,3,4,5,6,7,8,9,10
	y=x+y
	print(y)
print("1~10까지 합은:",y)
print()

y2=0
for x2 in range(1,11,2):
	y2=x2+y2
	print(y2)
print("1~10까지의 홀수 합은",y2)
print()

y3=0
for x3 in range(0,11,2):
	y3=x3+y3
	print(y3)
print("1~10까지의 홀수 합은",y3)	