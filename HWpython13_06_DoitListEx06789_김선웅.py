#HWpython13_06_DoitListEx06_김선웅.py

#리스트 요소 추가  append()
a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

#리스트 정렬 sort()
a=[1,4,3,2]
a.sort()
print(a)

a=['a','c','b']
a.sort()
print(a)

print("-"*30)

#리스트 뒤집기(reverse)
a=['a','c','b']
a.reverse
print(a)
print("-"*30)

#위치변환(index)
a=['a','c','b']
print(a.index('b'))
print("-"*30)

a=[1,2,3]
a.insert(0,4)#0자리에 4를 넣어라
print(a)
a.insert(3,5)#3자리에 5를 넣어라 그 자리는 뒤로 밀림
print(a)

print("-"*30)


#리스트 요소 제거(remove)
a=[1,2,3,1,2,3]
a.remove(3) #앞에거 하나만 삭제
print(a)

print("-"*30)

#리스트 요소 꺼내기
a=[1,2,3]
print(a.pop())
print(a)
print("-"*30)

#리스트에 포함된 요소 x의 개수 세기 count
a=[1,2,3,1]
print(a.count(1))
print("-"*30)

#리스트 확장 extend(x)  원래의 a리스트에 x리스트를 더한다

a=[1,2,3]
a.extend((4,5))
print(a)
a.extend("nice")
print(a)






