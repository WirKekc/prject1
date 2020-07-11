keywords = []
with open('table1.txt') as a:
    for line in a:
        keywords.append(line.strip())
print('"', end="")
print(*keywords, sep='\t')
print('"')