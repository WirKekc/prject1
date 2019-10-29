sentence = input().split()
list_len = []
d = {}

for i in sentence:
    list_len.append(len(i))

for i in sentence:
    d.update({len(i): list_len.count(len(i))})

print(*["{0}: {1}".format(i, d[i]) for i in sorted(d.keys())], sep="\n")
