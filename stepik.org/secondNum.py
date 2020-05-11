a = input().split()
a.sort()
# b = []
# for i in range(len(a)):
#     if a[i] == a[i-(len(a)-1)]:
#         b.append((a[i]))
rep_list = [x for x in a if a.count(x) > 1]
print(*set(rep_list))
