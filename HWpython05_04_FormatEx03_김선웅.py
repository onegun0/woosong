#HWpython05_04_formatEx03_김선웅

test1= "Error in %d%%" %98
print(test1)


#오른쪽 정렬
test2= "%10s" %("hi1234")
print(test2)

#왼쪽 정렬
test3= "%-10s" %("hi1234")
print(test3)

#소숫점 자리수
test4= "%0.4f" %3.42123412
print(test4)

#십의자리와 소숫점 자리수
test5= "%10.4f" %3.42123412
print(test5)