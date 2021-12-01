#HWpython10_09_ListW3Chk09CopyWarmUp_김선웅
'''
01.
Copy a List
list2 = list1는 카피가 아니라 주소를 참조한 것이다(reference)

result01=list([1, 2, 3]) #10번 주소에 저장 생성자를 따로 쓰면 따로 저장가능
result02=list([1, 2, 3]) #20번 주소에 저장

result02=result01 #이 경우 result02는 result01의 주소 값을 참조한 것


02
'''

result01=list([1, 2, 3])
result02=result01 
print(result01)
print(result02)


result01[1]="orange" #result01만 값을 변경했는데 result02도 같이 바뀜
print(result01)
print(result02)



print("="*20)

result01=list([1, 2, 3]) #생성자 사용
result02=list([1, 2, 3]) #생성자 사용
print(result01)
print(result02)


result01[1]="orange" #result01 변경 result02는 따로인 값
print(result01)
print(result02)