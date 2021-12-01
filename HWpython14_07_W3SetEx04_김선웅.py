#HWpython14_07_W3SetEx04_김선웅

#isdisjoint():중복이 있으면 True
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z) 

#issubset(): x가 중심 모든 값이 중복되어야 True
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issuperset() y가 중심. 모든 값이 중복되어야 True 
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)