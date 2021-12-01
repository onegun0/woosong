#HWpython09_04_exam06_empList06_김선웅

'''


사번,사원명, 직위, 멘토사번, 입사일, 급여, 보너스, 부서번호 코드북


검색할 직업을 입력하세요
직업이 MANAGER, SALESMAN 직원 리스트
스플릿 이용
'''
import csv

file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)

listemp=list(emp_csv)


print(listemp)


job=input("검색할 직업을 입력하세요=").upper()
job1=job.split(',') #split 하면 리스트화 됨

print(f"직업이 {job} 직원 리스트")
title=["이름","직업","   급여"]
print("-"*30)
for t in title:
	print(t,"	 ", end="")
print()
print("-"*30)

for emp in listemp:
	for x in range(len(job1)):
		if emp[2]== job1[x].strip():
			print(emp[1],"	",emp[2],"	",emp[-3])	







'''
print(f"직업이 {job} 직원 리스트")
title=["이름","직업","급여"]
print("-"*30)
for t in title:
	print(t,"	 ", end="")
print()
print("-"*30)


for listemp in emp_csv :
	for x in range(len(job1)):
		if listemp[2]==job1[x].strip() :
			print(f"{listemp[1]}	{listemp[2]}   {listemp[-3]}")
'''	