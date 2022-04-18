import collections
n = int(input())
a = [int(x) for x in input().split()[:n]]
d = list()
f = 0
a.sort(reverse = True)
counter = collections.Counter(a)
for i in range (max(a)+1):
    if counter[i] > 2:
        print("NO")
        f = 1
        break
    elif counter[i] == 2:
        d.append(i)
d.sort()
if (f != 1):
    print("YES")
    print(len(d))
    d = [str(x) for x in d]
    print(' '.join(d))
    a = list(dict.fromkeys(a))
    a = [str(x) for x in a]
    print(len(a))
    print(' '.join(a))
