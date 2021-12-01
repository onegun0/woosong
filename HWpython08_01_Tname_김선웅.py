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
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]


for menu in TName:
	print("\t",menu, end="\t")
print()
print("-"*70)

for emp in empInfo:
	print(emp[0][0].lower())



'''
	if emp[0][0].lower() ==t: 
		emp[0]="계약직"
'''