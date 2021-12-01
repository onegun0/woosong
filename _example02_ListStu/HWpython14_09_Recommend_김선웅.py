import csv

file = open('./../_dataSet01/groupList.csv','r')
grouplist = csv.reader(file)
glist= list(grouplist)

a = []
vlist = []
group1 = []

for x in glist:
	a = x
print("원본 데이터 a=", a)


for va in a:
	if len(va) >= 3:
		vlist.append(va[-2:])
	else:
		vlist.append(va)
print()
print("vlist 이름만 가져오기=", vlist)
print()

for vvlist in vlist:
	x = vlist.count(vvlist), vvlist
	group1.append(x)

s1=set(group1)
group1=list(s1)
print("중복 삭제=",group1)
print()
group1.sort(reverse=True)
for g in range(len(group1)):
	print(f"{g+1}번: {group1[g][1]}  {group1[g][0]}")


