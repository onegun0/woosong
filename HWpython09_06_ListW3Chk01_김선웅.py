#HWpython09_06_ListW3Chk01_김선웅
'''
**collection Type: 하나의 변수에 여러개 저장 가능, 
01. List : 순서(인덱스 관리), 바꾸기 가능, 중복 가능, [ ] 대괄호 사용  
02. Tuple : 순서(인덱스 관리), 바꾸기 불가능, 중복 가능, ( ) 소괄호 사용
03. Set : 순서 없음, 바꾸기 불가능, 인덱스값 없음, 중복 불가능, { } 중괄호 사용
04. Dictionary : 순서 있음(key), 바꾸기 가능, 중복 불가능(key), { } 중괄호 사용
'''
#연습01
mylist=["apple", "banana","cherry"]

#연습02(indexed)
thislist=["apple", "banana","cherry"]
print(thislist)

#연습03(Duplicates)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#연습04(len())
thislist=["apple","banana","cherry"]
print(len(thislist))

#연습05(any data Type)
list1=["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#연습06(different data type)
list1=["abc", 34, True, 40, "male"]

#연습07(type)
mylist=["apple", "banana", "cherry"]
print(type(mylist))

#연습08(Constructor)
thislist=list(("apple","banana","cherry"))
print(thislist)