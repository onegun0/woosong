#HWpython11_06_StuDataAgeSex_김선웅


import csv

file=open('./../_dataSet01/StuDataSet02.csv','r')
stu_csv=csv.reader(file)


print(stu_csv)

print("이름	나이	성별")
print("="*20)


	

for listemp in stu_csv:


	if (listemp[2][7]=="3") or (listemp[2][7]=="4"):
		age = "20"
	elif (listemp[2][7]=="1") or (listemp[2][7]=="2"):	
		age = "19"
	vage =2021-(int(age+listemp[2][0:2]))
	

		


	
	
	if (listemp[2][7:8] == "2") or ((listemp[2][7:8] == "4")) :
		gen="여자"
	elif (listemp[2][7:8] == "1") or ((listemp[2][7:8] == "3")):
		gen="남자"


		print(f"{listemp[1]}	{vage}	{gen}")


	