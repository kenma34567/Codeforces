n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(a[(n+1)//2-1])
"""d = dict()
for i in range(n):
    distance = 0
    for j in range(n):
        distance += abs(a[i]-a[j])
    d.update({f'{a[i]}' : distance})
x = list()
y = d.items()
for i in y:
    if i[1] == min(d.values()):
        x.append(i[0])
x.sort()
print(x[0])"""


