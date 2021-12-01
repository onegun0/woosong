#HWpython04_06_AutoMachine_step03_김선웅



price=[1000,2500,1500,2000,2000]
menu=['orange','strawbarry','peach','mango','grape','종료']
idx=0


while True:
	print("\n","****** 우송대학교 과일 판매머신 v03*******")
	

	
	while True:
		if(idx==len(menu)-1):
			print(idx+1,"",menu[idx])
			break
		print(idx+1,"",menu[idx],":",price[idx],"원")
		idx+=1
	
	num=int(input("구매번호를 입력하세요"))
	
		
	if num<len(menu):
		print("%s : %d원입니다" %(menu[num-1],price[num-1]))
	else:
		print("종료합니다")
		break