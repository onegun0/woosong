#HWpython14_02_DoitSetEx02_김선웅

#1 교집합_동일한 결과 2가지 방법   3가지 반환값이 있음
# 교집합, 합집합, 차집합 구하기
# set 자료형을 정말 유용하게 사용하는 경우는
# 교집합, 합집합, 차집합을 구할 때이다.

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

inter1=s1 &s2
inter2=s1.intersection(s2) #교집합
print(inter1)
print(inter2)


vuni1=s1|s2
vuni2=s1.union(s2)			#합집합
print(vuni1)
print(vuni2)


differ1 = s1 - s2
differ2 = s2 - s1

differ3 = s1.difference(s2)  #차집합
differ4 = s2.difference(s1)
print(differ1)
print(differ2)
print(differ3)
print(differ4)

