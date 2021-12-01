
'''
^ 4인 이상 명수를 확인하세요

'''


import random
rand=[]


while True:	
	person=input("4인 이상의 이름을 입력하세요.(종료:0):")
	vperson = person.strip().split()
	#print(vperson)   [a,d,f,g]
	num = random.randint(1,len(vperson))
	rand.append(num)
	if person == "0":
		exit()
	elif len(vperson) < 4:
		print("^ 4인 이상 명수를 확인하세요")
	else:
		while True:
			for a1 in range(len(rand)) :            
				for a2 in range(a1): 
					if rand[a1] != rand[a2]:
						rand.append(num)
						
					else:
						num = random.randint(1,len(vperson))
						
			if len(rand) == len(vperson):
				break
		print(rand)

'''a=[a, s, d, f]
for a1 in range(len(a)) :            
	for a2 in range(a1): 
		if a[a1]<a[a2]:
			a[a1],a[a2]=a[a2],a[a1]
		print(a)
'''	
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

	
			
			
		