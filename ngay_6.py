# Cho mảng số nguyên A[] gồm N phần tử và số nguyên X ,
#  hãy đếm xem trong mảng có bao nhiêu số lớn hơn X và bao nhiêu số nhỏ hơn X.
'''
a = [] 
n =int(input("nhap so phan tu: "))
for i in range(n):
    x = int(input("nhap phan tu: "))
    a.append(x)
nho = 0
lon = 0
s = int(input("so: "))
for y in range(len(a)):
    if s < a[y]:
        lon += 1
    elif s > a[y]:
        nho += 1

print(f"co {lon} so lon hon {s}")
print(f"co {nho} so nho hon {s}")
'''

# Cho mảng số nguyên A[] gồm N phần tử, nhiệm vụ của bạn là in ra các phần tử là số chẵn ở chỉ số chẵn,
#  nếu mảng không tồn tại phần tử như vậy thì in ra "NONE".

'''
a = []
n = int(input("nhap so phan tu: "))
for i in range(n):
    x = int(input("nhap phan tu: "))
    a.append(x)
b = []
for y in range(len(a)):
    if y%2 == 0 and a[y]%2 == 0:
        b.append(a[y])
print(b)
'''
