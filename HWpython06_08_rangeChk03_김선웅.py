#HWpython06_08_rangerChk03_김선웅

a=[1,2,3,4]
result=[]
'''
for num in a:      #num=1,2,3,4
	result.append(num*3)    #=3,6,9,12
print(result)


result=[num*3 for num in a]
print(result)
'''




result=[num*3 for num in a if num%2==0]
print(result)
