#HWpython04_06_AutoMachine_step02_김선웅



price=[1000,2500,1500,2000,2000]
menu=['orange','strawbarry','peach','mango','grape','종료']



while True:
	print("\n","****** 우송대학교 과일 판매머신 v01*******")
	

	idx=0
	while True:
		if(idx==len(menu)-1):
			print(idx+1,"",menu[idx])
			break
		print(idx+1,"",menu[idx],":",price[idx],"원")
		idx+=1
	
	num=int(input("구매번호를 입력하세요"))
	
		
	
	