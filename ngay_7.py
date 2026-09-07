# Cho 4 số X, Y, Z, T là số nguyên được nhập từ bàn phím.

# Bạn hãy in ra 3 dòng

# Dòng 1 lần lượt 4 số Y,Z,X,T mỗi số cách nhau một dấu phẩy

# Dòng 2 in ra tổng 4 số

# Dòng 3 in ra giá trị của biểu thử X - Y + Z * T.

# (Chú ý giá trị của tích Z * T và giá trị của tổng 4 số có thể tràn kiểu dữ liệu int)
'''
x= float(input())
y= float(input())
z= float(input())
t= float(input())
tong = x+y+z+t
giatri = x-y+z*t

print(f"{x},{y},{z},{t}")
print(tong, giatri)
'''
# Cho 2 số x, y. Nhiệm vụ của bạn là tính x ^ y

# Gợi ý : Bạn cần ép giá trị của hàm pow sang long long, ko in ra trực tiếp pow(x, y) nó sẽ hiện thị ra số thực

# Ví dụ bạn nhập : 11 8 thử xem nó có in ra 214358881 hay nó in ra 2.14359e+08
'''
x = int(input())
y = int(input())
s = pow(x,y)
print(s)
'''

#Cho số nguyên dương N, nhiệm vụ của bạn là tính căn bậc 2 và căn bậc 3 của N.
'''
import math
n = int(input())
s = math.sqrt(n) 
c = math.cbrt(n)
print(c,s)
'''

#Hàm ceil : làm tròn lên số nguyên gần nhất,
#  floor : làm tròn xuống số nguyên gần nhất,
#  round : làm tròn số nguyên phụ thuộc vào phần thập phân.

#Cho số thực X nhiệm vụ của bạn là sử dụng 3 hàm trên để tìm số nguyên nhỏ hơn gần X nhất
# , số nguyên lớn hơn gần X nhất, số nguyên gần X nhất.
'''
import math
x = float(input())
s= math.ceil(x)
c = math.floor(x)
v = round(x)

print(s,c,v)

'''

# Cho nguyên dương N, bạn hãy sử dụng phép chia dư để lấy ra chữ số cuối cùng và 2 chữ số cuối cùng của N.
'''
n = int(input())
s = n%10
v = n%100

print(s,v)
'''
