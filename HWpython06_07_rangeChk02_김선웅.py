#HWpython06_07_rangerChk02_김선웅

a=[1,2,3,4]
result=[]
'''
for num in a:      #num=1,2,3,4
	result.append(num*3)    #=3,6,9,12
print(a)
print(result)
'''




result=[num*3 for num in a]
print(result)