#HWpython12_01_StuDataAgeBetween_김선웅


import csv

file=open('./../_dataSet01/StuDataSet02.csv','r')
stu_csv=csv.reader(file)

low=int(input("검색할 연령((하한)을 입력하세요="))
high=int(input("검색할 연령(상한)을 입력하세요="))


print("="*40)
print(f"{low}세 ~{high}세 학생 리스트")
print("="*40)
print("이름	나이	통신사 	전화번호")
print("-"*40)

for listemp in stu_csv:
	if (listemp[2][7]=="3") or (listemp[2][7]=="4"):
		age = "20"
	elif (listemp[2][7]=="1") or (listemp[2][7]=="2"):	
		age = "19"
	vage =2021-(int(age+listemp[2][0:2]))
	


	if low <= vage and vage <=high  :
		print(f"{listemp[1]}	{vage}	{listemp[4]}	{listemp[3]}")


'''
	if (listemp[2][7:8] == "2") or ((listemp[2][7:8] == "4")) :
		gen="여자"
	elif (listemp[2][7:8] == "1") or ((listemp[2][7:8] == "3")):
		gen="남자"
	
	if (vage >= 30) and ( listemp[4].strip() =="sk") :
		print(f"{listemp[1]}	{vage}	{listemp[4]}	{listemp[3]}")

'''



	