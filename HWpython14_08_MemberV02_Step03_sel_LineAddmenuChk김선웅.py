#HWpython12_03_MemberV02_Step03_sel_김선웅


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록','4. 회원탈퇴', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList=[]
temp=[]

for vmenu in range(len(menu)):
	menuChk.append(menu[vmenu][0])
print(menuChk)

me_len=len(menu)
print(me_len)

while True:
	print("{0:=^20}"*me_len.format("메뉴선택"))
	print()
	for m in menu:
		print(f"{m:^20}", end=" ")
	print("\n")
	print("="*94)
	print()
	num=input("{0:>50}".format("메뉴의 번호를 입력해주세요:"))
	print()
	if num in menuChk:
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
				print("{0:>50}".format("먼저 회원가입 해주세요."))
			else:
				print("{0:>50}".format("^member List !"))
				print()
				print("="*94)
				for vitem in itemList:
					print("{0:^15}".format(vitem),end="")
				print()
				print("="*94)
				for vList in userList:
					for List in vList:
						print("{0:^15}".format(List),end="")
					print()
				print()	
				print("-"*94)
			print()
		elif num=="9":
			print("\t""9. 메뉴를 종료합니다")
			print()
			break
			print()

	elif num != menuChk:
		print("{0:>50}".format("다시 입력해주세요"))
		print()
		print()
