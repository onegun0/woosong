#HWpython11_03_selectSortAnalysis02_김선웅

#오름차순
import random
a=[]
person=input("4인 이상의 이름을 입력하세요.:")
vperson = person.strip().split()
num = random.randint(1,len(vperson))
a.append(num)


a=[1,2,3,4]
#print(a) #x
for a1 in range(len(a)) :            
	for a2 in range(a1):       #outer loop        ~(len-1)   #inner loop        
		print(a1, a2)	
	