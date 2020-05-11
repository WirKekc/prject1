a = input().lower()
b = input().lower()
c = True
for i in a:
    if b.count(i) != a.count(i):
        c = False
        break
print(c)
