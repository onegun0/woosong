#HWpython07_13_strfunChk01_김선웅

a="hobby"

print(a.count("b"))
print(len(a)) 

#위치 알려주기
a="Python is the best choice"
print(a.find("b"))
print(a.find("k")) #값이 없으면 -1 반환

#위치 알려주기2
a="Life is too short"
print(a.index("t"))
print(a.index("k")) #값이 없으면 에러
