#HWpython06_10_Chap03_김선웅

#1
'''
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
print("shirt")
'''

#2
a=0
i=0
while i <= 1000:
	if i %3==0:
		a=a+i
	i+=1
print(a)

#3
i=0
	
while i<=5:
	i=i+1
	print("☆"*i)


#4	
for x in range(1,101):
	print(x)

#5
a=[70,60,55,75,95,90,80,80,85,10]
result=0
for score in a:
	result = score+result
print(result/len(a))

#6
number=[1,2,3,4,5]
result=[]
result = [n*2 for n in number if n % 2==1]
print(result)