#HWpython07_05_strChk01_김선웅


#1
#문자열은 작은따옴표와 큰따옴표로 표현


#2
print("hello")
print('hello')

#3
a="hello"
print(a)

#4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#6
a="hello, world"
print(a[1])

#7
for x in "banana":
	print(x)

#8
a="hello, world"
print(len(a))

#9
txt="The best things in life are free!"
print("free" in txt)

#10
txt="The best things in life are free!"
if "free" in txt:
	print("Yes, 'free' is present.")
#11
txt = "The best things in life are free!"
if "expensive" not in txt:
	print("No, 'expensive' is NOT present.")

