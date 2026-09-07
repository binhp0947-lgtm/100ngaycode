# def largestDivisibleSubset(nums):
#     if not nums:
#         return [] tạo 1 lit rỗng 
#
#     nums.sort()  sếp xếp lit theo chiều tăng đần 
#     n = len(nums)  số phần tử của lit 

#     dp = [1] * n          # dp[i]: độ dài tập con kết thúc tại i
#     parent = [-1] * n     # truy vết

#     max_len = 1
#     max_idx = 0

#     for i in range(n):
#         for j in range(i):
#             if nums[i] % nums[j] == 0:
#                 if dp[j] + 1 > dp[i]:
#                     dp[i] = dp[j] + 1
#                     parent[i] = j

#         if dp[i] > max_len:
#             max_len = dp[i]
#             max_idx = i

#     # truy vết kết quả
#     res = []
#     while max_idx != -1:
#         res.append(nums[max_idx])
#         max_idx = parent[max_idx]

#     return res[::-1]



# n = int(input("Nhập số phần tử: "))

# lst = []   # tạo list rỗng

# for i in range(n):
#     x = int(input(f"Nhập phần tử thứ {i+1}: "))
#     lst.append(x)

# print("Danh sách vừa nhập:", lst)
def hat():
    n =int(input("nhập số phần tử "))
    so = []
    for i in range(n):
        x = int(input(f"nhap phan tu thu {i+1}; "))
        so.append(x)
    so.sort()
    dp = [1] * n 
    parent = [-1] * n
    max_len = 1
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if so[i] % so[j] == 0 :
                if dp[j] + 1 > dp[i]:
                   dp[i] = dp[j] + 1 
                   parent[i] = j 
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i 

    truyvet = []
    while max_idx != -1 :
        truyvet.append(so[max_idx])
        max_idx = parent(max_idx)
    return truyvet[::-1]

  

print(hat())

