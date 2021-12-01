#HWpython10_04_ListW3Chk06_김선웅


#Loop Lists
#연습01 (Collection Type_item)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#연습02(index_len(), range())
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#연습03(While_len() 비교 증감)
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#연습04(for문 표현식 for_)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



#List Comprehension
#연습01(구분해서 새로운 리스트에 추가하기)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print(fruits)

#연습02(for_ if 표현식)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] #리스트 안에 문장이 들어가서 실행

print(newlist)
#newlist = [expression for item in iterable if condition == True]

#연습03
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#연습04(range(10))
newlist = [x for x in range(10)]
print(newlist)#0,1,2,3,4,5,6,7,8,9

#연습05(range(10), if)
newlist = [x for x in range(10) if x < 5]
print(newlist)

#연습06(리스트 내용 대문자로 변환)

newlists=[x.upper() for x in fruits]
print(newlists)
print(fruits)

#연습07(fruits 리스트를 'hello'로 초기화)
newlist = ["hello" for x in fruits]
print(newlist)

#연습08(바나나가 아니면 리스트에 넣고 바나나는 오렌지로 넣어라)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


