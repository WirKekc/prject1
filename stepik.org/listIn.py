a = input().split()
b = input()
s = set()
try:
    a.index(b)
except ValueError:
    print(None)

for i in range(len(a)):
    try:
        s.add(a.index(b, i))
    except ValueError:
        pass
s = sorted(list(s))
print(*s)

# k = 0
# for i in range(len(a)):
#     if b == a[i]:
#         print(i, end=" ")
#         k += 1
# if k == 0:
#     print(None)
