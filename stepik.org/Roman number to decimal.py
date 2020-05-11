a = input()
dic1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
res = 0
for i in range(len(a)):
    if i == len(a)-1:
        if dic1[a[i]] <= dic1[a[i - 1]]:
            res += dic1[a[i]]
    elif i != 0 and dic1[a[i]] > dic1[a[i - 1]]:
        continue
    elif dic1[a[i]] < dic1[a[i + 1]]:
        res += dic1[a[i + 1]] - dic1[a[i]]
    else:
        res += dic1[a[i]]
print(res)
