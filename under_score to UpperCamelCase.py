# a = input().split("_")
# for i in a:
#     print(i[0].upper()+i[1:], end="")

print(*[i[0].upper()+i[1:] for i in input().split("_")], sep="")
