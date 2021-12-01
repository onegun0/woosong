#HWpython12_03_MemberV02_Step03_sel_김선웅


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
userList=[]
temp=[]

while True:
	print("="*20,"메뉴선택","="*20)
	print()
	for m in menu:
		print(m, end=" ")
	print("\n")
	print("="*50)
	print()
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	print()
	if num=="1":
		print("\t\t","^SignUp !")
		for signUp in itemList:
			print(f"\t{signUp:<10}:",end="") 
			templist=input()
			temp.append(templist)
		userList.append(temp)
		
		for vList in userList:	
			print(vList)
		print(f"현재 회원수는 {len(userList)}명입니다")	
		print()
		#temp.clear() #클리어는 계속 남아 있어서 안됨
		temp=[]	#계속 생성되어서 가능 
		print()


	elif num=="2":
		print("\t""2. 로그인 알고리즘 chk")
		print()
	elif num=="3":
		if len(userList)==0:
			print("\t""먼저 회원가입 해주세요.")
		else:
			print("\t","^member List !")
			print()
			print("="*50)
			for vitem in itemList:
				print(vitem,"\t",end="")
			print()
			print("="*50)
			for vList in userList:
				for List in vList:
					print(List,"\t",end="")
				print()
			print()	
			print("-"*50)
		print()
	elif num=="9":
		print("\t""9. 메뉴를 종료합니다")
		print()
		break
	else:
		print("\t""다시 입력해주세요")
		print()

