#exam01_empList01

'''
01. 파일 오픈
	_dataSet01\emp2.csv
02. read
03.Type chk

--------------------
사원명     연봉
--------------------
xxx         xxxx

사번,사원명, 직위, 멘토사번, 입사일, 급여, 보너스, 부서번호 코드북
HWpython08_09_exam02_empList02_김선웅
'''
import csv

file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
listemp=list(emp_csv)
#print(emp_csv)

title=["사원명","연봉"]

print("-"*20)
for t in title:
	print(t," ", end="")
print()
print("-"*20)
'''
for empList in emp_csv:
	print(empList[1], " ",empList[5])
'''
for x in range(len(listemp)):
	print(listemp[x][1], end="	")
	print(listemp[x][5])


