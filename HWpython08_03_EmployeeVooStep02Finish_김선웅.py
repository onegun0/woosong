#HWpython08_02_ListExam01_김선웅

TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],                   #캔디출력 : empinfo[0][1]
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],                #for i in range(len(empInfo)):
	[200,12],				   #	print(empInfo[i][0][0])
	[300,9],
	[230,11],
	[150,12]
]


for menu in TName:
	print("",menu, end=" \t")
print()
print("-"*70)

for emp in empInfo:
	if emp[0][0].lower() == "t": 
		emp[0]="계약직"
	else:
		emp[0]="정규직"

for x in range(len(empInfo)):
		empInfo[x].append((empPayTable[x][0]*empPayTable[x][1]))
		print(empInfo[x][0],"\t",empInfo[x][1],"\t",empInfo[x][2],"\t",empInfo[x][3])

#print(empInfo)
#for Info in empInfo:
	
	
'''
for i in range(len(empInfo)):
	#print(empInfo[i][0][0])
	if empInfo[i][0][0].lower() =="t":
		print("계약직"
'''

 