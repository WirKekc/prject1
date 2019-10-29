import re
import requests

reqlist = []
for i in range(1, 39):
    req = requests.get('https://top100.rambler.ru/navi/?cat_open=0&rgn=0&range=day&statord=0&resourceId=558177&theme=1166&page='+str(i))
    if req.status_code == 200:
        for url in re.findall(r"Статистика по (http.*?://)(.*?)\n", req.text):
            reqlist.append(url[1])
a = list(set(reqlist))

for i in range(len(a)):
    if a[i][-1] == "/":
        a[i] = a[i][:-1]

a.sort()
print(*a, sep="\n")
# print(req.text)
