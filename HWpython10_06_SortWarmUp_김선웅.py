#HWpython10_07_ListW3Chk07Sort01_김선웅

#연습01 (ascending, by default)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #기본은 오름차순a~z 
print(thislist)

#연습02 (numerically)
thislist = [100, 50, 65, 82, 23]
thislist.sort() #작~큰
print(thislist)

#연습03(reverse=True 문자)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #(리버스=트루) -> 내림차순
print(thislist)

#연습04(reverse=True 숫자)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#연습05(function)-50가 가장 가까운 순서로 정렬
def myfunc(n):
  return abs(n - 50) #abs는 절대값을 반환 

thislist = [100, 50, 65, 82, 23] #[50, 0, 15, 32, 27]
thislist.sort(key = myfunc) #괄호없음
print(thislist)