from collections import Counter

score = input().split()
# Способ 1
# print("%.2f" % (score.count('A')/len(score)))


# Способ 2 (Counters)
c = Counter(score)
print("%.2f" % (c['A']/len(score)))