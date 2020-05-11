def modify_list(l):
    # Способ 1
    # p = []
    # for i in l:
    #     if i % 2 == 0:
    #         p.append(i // 2)
    # l.clear()
    # for i in p:
    #     l.append(i)

    # Способо 2
    # l[:] = [i//2 for i in l if i%2 == 0]

    # Способ 3
    for i in range(len(l)):
        p = l.pop(0)
        if p%2 == 0:
            l.append(p//2)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]