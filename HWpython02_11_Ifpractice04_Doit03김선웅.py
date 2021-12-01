#HWpython02_11_Ifpractice04_Doit03김선웅


money= int(input("돈을 입력해주세요")) 
card= input("카드가 있다면 true를 없으면 false입력")



'''
if card=="true":
	card=True
elif card=="false":
	card=False
'''

#False : card =0 / True : card = 1

if money >= 3000 or card:
	print("택시 사용 가능")
else:
	print("걸어가라")