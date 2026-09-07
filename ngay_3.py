
i = input()
id = []
idx = 0
for _ in range(len(i)):
    if i[_] == '/':
        idx = _
        id.append(idx)

d = i[0 : id[0]]
m = i[id[0] + 1: id[1]]
y = i[ id[1] + 1 : len(i)]

if len(d) == 1:
    d='0' + d
if len(m) == 1:
    m='0' + m

print(f"{d}/{m}/{y}")
  

  #  nhap ngay thang :    /    /
 # dd/mm/yyyy
