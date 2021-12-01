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
b=0
while a <= 1000:
	if a % 3==0:
		b = b + a
	a += 1
print(b)
	
#3
star=0
while star<=5:
	print("*"*star)
	star+=1

#4
for x in range(1,101):
	print(x)

#5
a=[70,60,55,75,95,90,80,80,85,100]
result=0
for score in a:
	result+=score
print("평균:",result/len(a))

#6
number=[1,2,3,4,5]
result=[]
for n in number:
	if n % 2==1:
		result.append(n*2)
print(result)

result=[n*2 for n in number if n%2==1]
print("리스트 내포:",result)