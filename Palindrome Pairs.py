def count_single(string):
    co = 0
    dd = dict()
    for k in string:
        if not k in dd:
            dd.update({f'{k}': 1})
        else:
            dd[f'{k}'] += 1
    for v in dd.values():
        if v%2 != 0:
            co += 1
    return co

n = int(input())
a = []
output = 0
for i in range(n):
    a.append(input())
for i in range(n-1):
    for j in range(i+1, n):
        c = a[i] + a[j]
        if len(c) % 2 != 0: # odd
            if count_single(c) == 1:
                output += 1
        else:               # even
            if count_single(c) == 0:
                output += 1
print(output)