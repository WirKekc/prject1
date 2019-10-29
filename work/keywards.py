keywords = []
with open('keywords.txt') as a:
    for line in a:
        keywords.append(line.strip())
print('"', end="")
print(*keywords, sep='","', end="")
print('"')
