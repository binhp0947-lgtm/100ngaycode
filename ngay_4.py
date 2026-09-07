import math
# i = []
# n = int(input(" so phan tu"))
# for y in range(n):
#     x = int(input("nhap so"))
#     i.append(x)
# b = []
# for a in range(n):
#     if a <=2 :
#         b.append(a)
#     else:
#         for c in range(2,a**0.5 + 1):
#             if a%c == 0:
#                 b.append(a)

# for d in list(b):
#     d=sum(b)
   

# print(d)

def snt(a):
    if a < 2:
        return False
    for i in range (2 , int(math.sqrt(a))+1 ):
        if a%i ==0:
            return False
    return True

n = int(input())
st = []

for i in range(n):
    t = int(input())
    if snt(t):
        st.append(t)

sum = 0
for i in st:
    sum += i

print(f"{sum/len(st):.3f}")