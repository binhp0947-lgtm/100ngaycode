'''
import numpy
x = float((input("nhap so dien")))
x = numpy.abs(x)
if x>=0 and x<=50:
    x = x*2000
    print(x)
elif x>=51 and x<=100:
    x = x*2500
    print(x)
else:
    x = x * 3000
    print(x)

'''
#S = (A[0]^0 + A[1]^1 + A[2]^2 + …. + A[N-1]^(N-1)) % 1000000007
'''
a = []
n = int(input("so phan tu: "))
for i in range(n):
    x = int(input("nhap phan tu: "))
    a.append(x)

y = 0
for t in range(n):
    r = t
    y += a[t]**r
    
print(y)
'''
#Cho mảng A[] gồm N phần tử bạn hãy tìm 2 số A[i] và A[j] trong mảng với A[i] = A[j] và i < j sao cho j - i đạt giá trị lớn nhất.
a = []
n = int(input("so phan tu: "))
for i in range(n):
    x= int(input(" nhap phan tu: "))
    a.append(x)
s = 0
for y in range(n):
    for j in range(y):
        if a[y] == a[j] :

            s = max(s,y - j)
            print(s)
            print(a[y])
            print(a[j])
