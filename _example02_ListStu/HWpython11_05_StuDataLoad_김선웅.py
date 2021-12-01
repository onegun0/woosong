#HWpython11_05_StuDataLoad_김선웅


import csv

file=open('./../_dataSet01/StuDataSet02.csv','r')
stu_csv=csv.reader(file)


print(stu_csv)

print("이름	나이	성별")
print("="*20)

for listemp in stu_csv:
	age=2021-int(listemp[2][:2])-2000
	

	if (listemp[2][7:8] == "2") or ((listemp[2][7:8] == "4")) :
		gen="여자"
	else:
		gen="남자"
	

	print(f"{listemp[1]}	{age}	{gen}")


