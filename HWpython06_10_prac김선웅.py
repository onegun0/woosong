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




result=[f"{outer}*{inner}={inner*outer}" for outer in range(2,10) for inner in range(2,10) ]
print(result)
