#HWpython09_01_exam03_empList03_김선웅

'''


사번,사원명, 직위, 멘토사번, 입사일, 급여, 보너스, 부서번호 코드북



검색할 연봉 하한값 입력하세요:2500
검색할 연봉 상한값 입력하세요:3000
연봉2500~3000인 사원 리스트

----------------------
이름          연봉
'''
import csv

file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
listemp=list(emp_csv)




ha=int(input("검색할 연봉 하한값을 입력해주세요="))
sang=int(input("검색할 연봉 상한값을 입력해주세요="))
print(f"연봉 {ha} ~{sang}인 사원 리스트")
title=["사원명","연봉"]
print("-"*20)
for t in title:
	print(t," ", end="")
print()
print("-"*20)

for x in range(len(listemp)):
	if ha <=int(listemp[x][5])<= sang :
		print(f"{listemp[x][1]}	{listemp[x][5]}")
