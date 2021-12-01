#HWpython09_07_ListW3Chk02_김선웅
'''
**collection Type: 하나의 변수에 여러개 저장 가능, 
01. List : 순서(인덱스 관리), 바꾸기 가능, 중복 가능, [ ] 대괄호 사용  
02. Tuple : 순서(인덱스 관리), 바꾸기 불가능, 중복 가능, ( ) 소괄호 사용
03. Set : 순서 없음, 바꾸기 불가능, 인덱스값 없음, 중복 불가능, { } 중괄호 사용
04. Dictionary : 순서 있음(key), 바꾸기 가능, 중복 불가능(key), { } 중괄호 사용
'''
#연습01
thislist=["apple", "banana", "cherry"]
print(thislist[1])

#연습02
thislist=["apple", "banana", "cherry"]
print(thislist[-1])

#연습03
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#연습04
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#연습05
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#연습06
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#연습07
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
	print("Yes, 'apple' is in the fruits list")