#HWpython07_08_strChk04Format_김선웅

#concatenate
#1
a="Hello"
b="World"
c=a+b
print(c)

#2
a="hello"
b="World"
c=a+"     "+b
print(c)

#Format
#1
age=36
txt="My name is John, and I am {}"
print(txt.format(age))

#2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#4
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt= 'We are the so-called "Vikings" from the north.'
print(txt)