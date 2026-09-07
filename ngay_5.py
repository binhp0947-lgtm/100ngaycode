# # Cho mảng số nguyên A[] gồm N phần tử, nhiệm vụ của bạn là đếm xem trong mảng có bao nhiêu số chẵn,
#  bao nhiêu số lẻ, tổng các phần tử là số chẵn, tổng các phần tử là số lẻ.
# a =[]
# sochan = 0
# sole = 0 
# tongc = 0
# tongl = 0
# n = int(input("nhap so phan tu: "))
# for i in range(n):
#     x = int(input("nhap phan tu: "))
#     a.append(x)
#     if x%2 == 0 :
#         sochan += 1
#         tongc += x 

#     else:
#         sole += 1
#         tongl += x

# print(f"co {sole} so le, co {sochan} so chan"),
# print(f"tong cua so chan: {tongc}")
# print(f"tong cua so le: {tongl}")


# Cho mảng số nguyên A[] gồm N phần tử, hãy đếm xem trong mảng của bạn có bao nhiêu số có cùng giá trị nhỏ nhất. 
# Ví dụ mảng A = {1, 2, 1, 3, 5} thì số nhỏ nhất trong mảng là 1 xuất hiện 2 lần.

a = []
sonho = 10**7
solap = 0
n = int(input("nhap so phan tu: "))
for i in range(n):
    x =int(input("nhap phan tu: "))
    a.append(x)
for y in range(len(a)):
    if sonho > a[y]:
        sonho = a[y]

    if sonho == a[y]:
        solap += 1    
    

print(f"so nho nhat trong mang: {sonho}",f"xuat hien: {solap} lan")