text = []
with open('text.txt') as a:
    # reader = csv.reader(a, delimiter=";")
    for line in a:
        # b = line[1].encode('windows-1251').decode('utf8')
        # print(line)
        text.append(line.strip().lower())

l = set(text)
print(*sorted(l), sep='\n')
