
'''
^ 4인 이상 명수를 확인하세요

'''


import random
rand=[]
while True:	
	person=input("4인 이상의 이름을 입력하세요.(종료:0):")
	vperson = person.strip().split()
	#print(vperson)   [a,d,f,g]

	if person == "0":
		exit()
	elif len(vperson) < 4:
		print("^ 4인 이상 명수를 확인하세요")
	else:
		while True:
			num = random.randint(1,len(vperson))#4
			rand.append(num)
			for x in rand:
				for y in range(len(vperson)):
					if  num[y] != rand[x] :
						rand.append(num)
			print(rand)
				
					
				
					

			



'''	
		for vname in vperson:
			print(vname, end="\t")
		print()
		print()
		for x in range(len(rand)):
			print(rand[x], end="\t")
		print()
		print("-"*30)
		print()
'''			

	
			
			
		