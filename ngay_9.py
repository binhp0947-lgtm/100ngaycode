# bài toán đề quy cơ bản
"""
def con(n):
    if n <= 2 :
        return 1
    else:
        return min(con(n-1), con(n-2)) +1
    

n = int(input())
print (f"cach nahy it nhat de den coc {n} la: {con(n)}")
"""
#Cho mảng A[] gồm N phần tử là các số nguyên, bạn hãy thực hiện phép tính cộng hoặc trừ N số nguyên này theo hướng dẫn.
# Bạn được cấp 1 mảng B[] gồm N - 1 phần tử đại diện cho N - 1 phép toán giữa N phần tử ban đầu trong mảng, 
# trong đó 1 tương ứng với phép cộng và 2 tương ứng với phép trừ.

a = []
b = []
n = int(input("so phan tu: "))
for i in range(n):
    j = int(input("phan tu a: "))
    a.append(j)
for p in range(n-1):
    k = int(input("phan tu b: "))
    b.append(k)
c=[]
for k in range(len(b)):
    if b[k] == 1 :
        c.append ( a[k+1] + a[k])
    if b[k] == 2 :
        c.append(a[k]+a[k+1])
if b[k] !=2 and b[k] != 1 :
    print("loi !! vui long nhap 0 va 1 vao bang b[]")
print(c)
