#HWpython11_03_selectSortAnalysis02_김선웅

#오름차순
a = [75, 65, 100, 80, 90, 55, 95, 30, 20, 50]

for a1 in range(len(a)) :  #outer loop        ~(len-1)
	for a2 in range(a1+1): #inner loop        
		if a[a1]<a[a2]:
			a[a1],a[a2]=a[a2],a[a1]
print(a)