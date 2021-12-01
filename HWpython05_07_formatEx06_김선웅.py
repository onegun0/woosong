#HWpython05_05_formatEx04_김선웅

str01="My name is {}".format("Kim")
print(str01)

int01="{1}+{0}={2}".format(10,20,(10+20))#format(0,1,2)
print(int01)


int01= "{idx1}+{idx2}={idx3}".format(idx2=10,idx1=20,idx3=(10+20))#변수 대입가능
print(int01)