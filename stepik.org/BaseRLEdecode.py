a = input()
b = ""
for i in range(len(a)):
    if a[i].isalpha():
        b += a[i] + " "
    else:
        b += a[i]
c = ""
dig = ""
b = b.split()
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j].isdigit():
            # c += (int(b[i][0])*b[i][1])
            dig += b[i][j]
        if b[i][j].isalpha():
            if dig != "":
                c += int(dig) * b[i][j]
                dig = ""
            else:
                c += b[i][j]
print(c)

#
# n = input()
# num = 0
# for l in n:
#     if not l.isdigit():
#         if num == 0:
#             print(l, end='')
#         else:
#             print(l*num, end='')
#         num = 0
#     else:
#         num = num*10 + int(l)
