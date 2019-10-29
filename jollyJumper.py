a = input().split()
res = []
for i in range(len(a)-1):
    res.append(abs(int(a[i])-int(a[i+1])))

if len(a) > 0:
    b = [i+1 for i in range(len(a)-1)]
else:
    b = [1]

if b != sorted(res):
    print("Not jolly")
else:
    print("Jolly")

# Способ 2
# 
# a = [int(i) for i in input().split()]
print('Jolly' if sorted([abs(a[i]-a[i+1]) for i in range(len(a)-1)]) == [i for i in range(1,len(a))] else 'Not jolly')
