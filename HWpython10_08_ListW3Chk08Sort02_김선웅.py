#HWpython10_08_ListW3Chk08Sort02_김선웅

#연습06(case Insensitive Sort) default case senstive: ASCll A65/a97

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() #대문자 먼저 나오고 소문자 순서(아스키 코드라서)
print(thislist)

#연습07(운좋게 우리는 빌트인 함수를 사용할 수 있다)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #모두 소문자로 변경
print(thislist)

#연습08(reverse()) 현재 상태에서 자리를 바꿔줌
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() 
print(thislist)