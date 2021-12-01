#HWpython05_12_Exam01_김선웅
'''
1번 학생 90점 합격입니다.
2번 학생 30점 불합격입니다.
3번 학생 60점 합격입니다.
4번 학생 50점 불합격입니다.
5번 학생 80점 합격입니다.

grade=[90,30,60,50,80]
for score in grade:
	print(score)

print(len(grade))

for score in range(len(grade)): #range(5)>>0 1 2 3 4 
	print(grade[score])
'''
grade=[90,30,60,50,80]

'''
for score in range(len(grade)): #range(5)>>0 1 2 3 4 
	if grade[score]>=60:
		print("%d번 학생 %3d점 %3s 입니다." %(score+1,grade[score], "합격"))
	else:
		print("%d번 학생 %3d점 %3s 입니다." %(score+1,grade[score],"불합격"))
	'''
'''
for score in range(len(grade)):
	if (grade[score]>=60):
		hapgyuk="합격"
	else :
		hapgyuk="불합격"
	print("%d번 학생 %3d점 %3s입니다." %(score+1,grade[score],hapgyuk))

'''
'''
for score in range(len(grade)):
	jumsu=grade[score]
	print(f"{score+1}번 학생 {jumsu}점 합격"if jumsu >=60 else f"{score+1}번 학생 {jumsu}점 불합격")
'''
for score in range(len(grade)):
	result="합격" if grade[score]>=60 else "불합격"
	print("%d번 학생 %d점 %s입니다" %(score+1, grade[score], result))