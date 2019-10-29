a = input()
b = input()
s = set()

if a.find(b) == -1:
    print(a.find(b))
else:
    for i in range(len(a)):
        if a.find(b,i) != -1:
            s.add(a.find(b, i))
    s = sorted(list(s))
    print(*s, sep=" ")


