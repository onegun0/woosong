#HWpython02_03_IFpractice01_김선웅
#실행시 id와 PW를 입력 받기

vid = "orange"
vpw = "1234"

vvid = input("id를 입력하세요:")
vvpw = input("pw를 입력하세요:")

if vvid == vid: 
	if vvpw== vpw:
		print("로그인 성공")
	else: 
		print("비밀번호를 확인하세요")
elif vid != vvid:
	if vpw==vvpw:
		print("아이디를 확인하세요")
	else:
		print("아이디와 비밀번호를 확인하세요")
