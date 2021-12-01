
'''
^ 4인 이상 명수를 확인하세요

'''


import random
rand=[]


while True:	
	person=input("4인 이상의 이름을 입력하세요.(종료:0):")
	vperson = person.split()
	
	if person == "0":
		exit()
	elif len(vperson) < 4:
		print("^ 4인 이상 명수를 확인하세요")
	else:
		while True:
			if len(rand) == len(vperson):
				break
			num = random.randint(1,len(vperson))
			if num not in rand:
				rand.append(num)
		
		
		
		for vname in vperson:
			print(vname, end="\t")
		print()
		print()
		for x in range(len(rand)):
			print(rand[x], end="\t")
		print()
		print("-"*30)
		print()
			

	
			
			
		