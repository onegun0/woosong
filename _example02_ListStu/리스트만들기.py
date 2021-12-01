a= ['민교','강경태', '고재호', '김태인', '한현기','재호','민교','재호','선웅','박연희','민교', '선웅', 
'강경태', '고재호', '김태인', '한현기', '이준혁','민교', '선웅','임재우','민교','강경태','경태','경태']
vlist=[]
for va in a:
	if len(va)==3:
		vlist.append(va[1:])
	else:
		vlist.append(va)
print("이름만:",vlist)
print("민교=",vlist.count('민교'),"표")
print("재우=",vlist.count('재우'),"표")
print("재호=",vlist.count('재호'),"표")
print("준혁=",vlist.count('준혁'),"표")
print("선웅=",vlist.count('선웅'),"표")
print("현기=",vlist.count('현기'),"표")
print("경태=",vlist.count('경태'),"표")
print("태인=",vlist.count('태인'),"표")
print("연희=",vlist.count('연희'),"표")
#민교', '재우', '재호', '준혁', '선웅', '현기', '경태', '태인', '연희
s1=set(vlist)
vvlist=list(s1)
print("집합:",s1)
vvlist.sort()
print("오름차순:",vvlist)

		