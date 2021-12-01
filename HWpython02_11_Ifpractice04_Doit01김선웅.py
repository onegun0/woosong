#HWpython02_11_Ifpractice04_Doit01김선웅


money = input("돈이 있나요? true or false를 입력하세요:")

if money== "true":
	money=True
elif money=="false":
	money=False

print(type(money))

if money:
	print("택시 사용 가능")
else:
	print("걸어가라")
