#HWpython11_03_selectSortFinish_김선웅

#오름차순
a = [75, 65, 100, 80, 90, 55, 95, 30, 20, 50]
print("소트 전",a)
for a1 in range(len(a)-1) :  #outer loop        ~(len-1) 0~9까지 -1안하면 10번 인덱스까지 돌아감
	for a2 in range(a1+1,len(a)): #inner loop        range(num~num)까지 이용해서 헛도는 것 방지
		print(a1,a2)
		if a[a1]>a[a2]:
			a[a1],a[a2]=a[a2],a[a1]




print("소트 후",a)





for a1 in range(len(a)-1) :  #outer loop        ~(len-1) 0~9까지 -1안하면 10번 인덱스까지 돌아감
	for a2 in range(a1+1,len(a)): #inner loop        range(num~num)까지 이용해서 헛도는 것 방지
		if a[a1]<a[a2]:
			a[a1],a[a2]=a[a2],a[a1]
print("내림차순",a)