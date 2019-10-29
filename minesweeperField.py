rows, columns = map(int, input().split())

field = []
for x in range(rows):
    row = []
    inp = input()
    for y in range(columns):
        row.append(inp[y])
    field.append(row)

field_res = [[0 for i in range(columns)] for j in range(rows)]

for x in range(rows):
    for y in range(columns):
        mines_around = 0

        # if x == 0 and y == 0:
        #     if field[x + 1][y] == '*':
        #         mines_around += 1
        #     if field[x + 1][y + 1] == '*':
        #         mines_around += 1
        #     if field[x][y +1] == '*':
        #         mines_around += 1
        # elif x == 0 and y == columns - 1:
        #     if field[x + 1][y] == '*':
        #         mines_around += 1
        #     if field[x + 1][y - 1] == '*':
        #         mines_around += 1
        #     if field[x][y - 1] == '*':
        #         mines_around += 1
        # elif x == rows - 1 and y == 0:
        #     if field[x - 1][y] == '*':
        #         mines_around += 1
        #     if field[x - 1][y - 1] == '*':
        #         mines_around += 1
        #     if field[x][y - 1] == '*':
        #         mines_around += 1
        # elif x == rows - 1 and y == columns - 1:
        #     if field[x - 1][y] == '*':
        #         mines_around += 1
        #     if field[x - 1][y - 1] == '*':
        #         mines_around += 1
        #     if field[x][y - 1] == '*':
        #         mines_around += 1
        #
        # elif x == 0 or y == 0 or x == rows - 1 or y == columns - 1:
        #     if x == 0:
        #         if field[x + 1][y] == '*':
        #             mines_around += 1
        #         if field[x + 1][y + 1] == '*':
        #             mines_around += 1
        #         if field[x + 1][y - 1] == '*':
        #             mines_around += 1
        #         if field[x][y + 1] == '*':
        #             mines_around += 1
        #         if field[x][y - 1] == '*':
        #             mines_around += 1
        #     if y == 0:
        #         if field[x][y + 1] == '*':
        #             mines_around += 1
        #         if field[x + 1][y + 1] == '*':
        #             mines_around += 1
        #         if field[x - 1][y + 1] == '*':
        #             mines_around += 1
        #         if field[x + 1][y] == '*':
        #             mines_around += 1
        #         if field[x - 1][y] == '*':
        #             mines_around += 1
        #     if x == rows - 1:
        #         if field[x - 1][y] == '*':
        #             mines_around += 1
        #         if field[x - 1][y + 1] == '*':
        #             mines_around += 1
        #         if field[x - 1][y - 1] == '*':
        #             mines_around += 1
        #         if field[x][y + 1] == '*':
        #             mines_around += 1
        #         if field[x - 1][y - 1] == '*':
        #             mines_around += 1
        #     if y == columns - 1:
        #         if field[x][y - 1] == '*':
        #             mines_around += 1
        #         if field[x + 1][y - 1] == '*':
        #             mines_around += 1
        #         if field[x - 1][y - 1] == '*':
        #             mines_around += 1
        #         if field[x + 1][y] == '*':
        #             mines_around += 1
        #         if field[x - 1][y] == '*':
        #             mines_around += 1
        #
        # else:
        if x + 1 < rows and field[x + 1][y] == '*':
            mines_around += 1

        if x - 1 >= 0 and field[x - 1][y] == '*':
            mines_around += 1

        if y + 1 < columns and field[x][y + 1] == '*':
            mines_around += 1

        if y - 1 >= 0 and field[x][y - 1] == '*':
            mines_around += 1

        if x + 1 < rows and y + 1 < columns and field[x + 1][y + 1] == '*':
            mines_around += 1

        if x + 1 < rows and y - 1 >= 0 and field[x + 1][y - 1] == '*':
            mines_around += 1

        if x - 1 >= 0 and y + 1 < columns and field[x - 1][y + 1] == '*':
            mines_around += 1

        if x - 1 >= 0 and y - 1 >= 0 and field[x - 1][y - 1] == '*':
            mines_around += 1

        # print(field)
        # print(field_res)
        field_res[x][y] = mines_around
        if field[x][y] == '*':
            field_res[x][y] = field[x][y]

for x in range(rows):
    print(*field_res[x], sep='')


