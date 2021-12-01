#HWpython05_06_formatEx05_김선웅
alignLeft  ="{1:<10}".format("nice day", "hi")
alignRight ="{:>10}".format("nice day")
alignCenter="{0:^10}".format("nice day")

#공백 채우기
spaceFil01="{:*^10}".format("hi")

print(alignLeft)
print(alignRight)
print(alignCenter)
print(spaceFil01)


x=342134234
y=3.42134234
floatEx1="{0:0.4f}{1:,d}".format(y,x)
