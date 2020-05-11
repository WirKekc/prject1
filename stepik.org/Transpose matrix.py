n, m = map(int, input().split())
matrix = [input().split() for i in range(n)]
for x in range(m):
    for y in range(n):
        print(matrix[y][x], end=" ")
    print()
# print(matrix)
