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

s=input("검색할 사원명을 입력해주세요=").upper()

for x in range(len(listemp)):
	if s==listemp[x][1]:
		print(f"{s} 사원의 연봉은 {listemp[x][5]}입니다")
