#Bạn đang đứng ở bậc thang thứ 0. Bạn cần leo lên đến bậc thang thứ n. Mỗi lần bạn có thể leo lên 1 bậc hoặc 2 bậc.

#Hỏi có bao nhiêu cách khác nhau để leo lên đến bậc thang thứ n?


def cau(i,cac={}):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 3
    if i > 3 :
        cac(i) = cau(i-1) + cau(i-2)
i = int(input("nhap so bac thang: "))
print(cau(i))