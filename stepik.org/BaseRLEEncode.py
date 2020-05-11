a = input()
res = ""
k = 0
if len(a) == 1:
    print(a)
else:
    a += "-"
    for i in range(len(a)):
        if a[i] == a[i-len(a)+1]:
            k += 1
        else:
            if k > 0:
                res += str(k+1)+a[i]
            else:
                res += a[i]
            k = 0
    print(res[:-1])
