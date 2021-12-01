import csv

file = open('./_dataSet01/groupList.csv', 'r')
grouplist = csv.reader(file)
glist = list(grouplist)
a = []
vlist = []
group = []

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
    x = vvlist, vlist.count(vvlist)
    group.append(x)

s1=set(group)
group=list(s1)
print("중복 삭제=",group)
print()
group.sort()
for g in range(len(group)):
    print(f"{g+1}번: {group[g][0]} {group[g][1]}")


