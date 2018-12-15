n, k = input().split()
n = int(n)
k = int(k)
a = []
for i in range(n):
    a.append(input())
a.sort(key = len)
correct = input()
dd = dict()
for i in range(n):
    if not a[i] in dd:
        dd.update({f'{a[i]}': i})
if correct in dd:
    c = dd[f"{correct}"]
    for i in range(n):
        if len(a[i]) == len(correct):
            if (i != c):
                a[c], a[i] = a[i], a[c]
            else:
                break
needed = 1
t = 0
for i in range(n):
    if a[i] != correct:
        needed += 1
        t += 1
        if t == k:
            t = 0
            needed += 5
    else:
        break
print(needed, end=" ")
needed = 1
t = 0
found = 0
for i in range(n):
    if a[i] != correct:
        needed += 1
        t += 1
        if t == k:
            t = 0
            needed += 5
    elif a[i] == correct:
        found = 1
    if found == 1 and i < n-1:
      if len(a[i+1]) > len(correct):
          break
print(needed, end="")

