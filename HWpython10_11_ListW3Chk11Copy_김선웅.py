#HWpython10_11_ListW3Chk11Copy_김선웅

#join List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2  #연산자 이용, 리스트+리스트로 넣기
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)	#for 문으로 하나씩 넣기

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2) #리스트 한번에 넣기
print(list1)