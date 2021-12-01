#HWpython09_03_exam05_empList05_김선웅

'''


사번,사원명, 직위, 멘토사번, 입사일, 급여, 보너스, 부서번호 코드북



사원중 보너스가 0이 아닌 사원 리스트 출력
보너스확인

'''
import csv

file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
listemp=list(emp_csv)


print("보너스 확인")
title=["이름","	","보너스"]
print("-"*20)
for t in title:
	print(t," ", end="")
print()
print("-"*20)

for x in range(len(listemp)):
	if int(listemp[x][-2]) !=0 :
		print(f"{listemp[x][1]}	   {listemp[x][-2]}")
