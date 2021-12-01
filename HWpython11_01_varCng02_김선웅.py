#HWpython11_01_varCng02_김선웅
#변수의 값 서로 변경

var01=100
var02=200
print("변경 전")
print("var01=", var01)
print("var02=", var02)

'''
var01=var02
print("var01=var02")
print("var01=",var01)
print("var02=",var02)

var01=100
var02=200

temp=var01
var01=var02
var02=temp           #일반적인 방법
'''
var01,var02=var02,var01 #파이썬에서 되는 방법
print("변경 후")
print("var01=",var01)
print("var02=",var02)