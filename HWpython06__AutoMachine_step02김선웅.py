#HWpython04_06_AutoMachine_step02_김선웅


num=0
price=[1000,2500,1500,2000,2000]
menu=['orange','strawbarry','peach','mango','grape','종료']



while True:
	print("\n","****** 우송대학교 과일 판매머신 v01*******")
	
	for num in range(len(menu)-1):
		print("%d. %s  %d원" %(num +1,menu[num] ,price[num]))

		
	print("="*50)
	
	
	num=int(input("구매번호를 입력하세요"))
	
	if num==1:
		print("오렌지 1000원입니다")
	elif num==2:
		print("딸기 2500원입니다")
	elif num==3:
		print("복숭아 1500원입니다")
	elif num==4:
		print("망고 2000원입니다")
	elif num==5:
		print("포도 2000원입니다")

	elif num==6:
		print("종료합니다")
		break

	
	
	

	
	
	