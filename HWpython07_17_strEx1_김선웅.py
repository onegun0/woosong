#HWpython07_17_strEx1_김선웅
'''
url: https://search.naver.com/search.naver
Qurty String
Where=nexearch
sm=top_hty
fbm=1&ie
ie=utf8
query=html
'''
s = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=html"
cng= s.split("?")
print(cng)    #cng=[https://search.naver.com/search.naver],[where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=html]
print("url="+cng[0])

cng2=cng[1].split("&")
print(cng2)

for x in range(len(cng2)): #cng2에서 0부터4까지(5번) 순서대로 x에 넣음
	print(cng2[x])            #where=nexearch, sm=top_hty, fbm=1, ie=utf8, query=html
print(len(cng2))              #5개