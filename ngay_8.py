# sắp sếp dãy số 
'''
a =[]
n = int(input("nhap so phan tu : "))
for i in range(n):
    x = int(input("nhap phan tu : "))
    a.append(x)
s = 0
for j in range(len(a)-1):
    for y in range(len(a)-1-j):
   
        if a[y] > a[y+1]:
            s = a[y]
            a[y] = a[y+1]
            a[y+1] = s 
print(a)
'''

# đổi tiền 
a =  [500000, 200000, 100000, 50000, 20000, 10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]
b = int(input("nhap so tien : "))
c =[]
for i in range(len(a)):
    s = b//a[i]
    c.append(s)
    b = b%a[i]

for i in range(len(a)):
    j =i
    if c[j] != 0:
        print(f"so to {a[i]}VND la {c[j]} to")
