n = int(input())
x = list()
for i in range(2*n-2):
    x.append(input())
y = x
y.sort(key=len)
s = list()
dd = dict()
s.append(y[0]+y[2*n-2-1])
s.append(y[2*n-2-1]+y[0])
s.append(y[0]+y[2*n-2-1-1])
s.append(y[2*n-2-1-1]+y[0])
s.append(y[1]+y[2*n-2-1])
s.append(y[2*n-2-1]+y[1])
s.append(y[1]+y[2*n-2-1-1])
s.append(y[2*n-2-1-1]+y[1])
for i in range(8):
    if not s[i] in dd:
        dd.update({f'{s[i]}': 1})
    else:
        dd[f'{s[i]}'] += 1
print(dd)
target = max(dd, key=dd.get)
print(target)
print(y)
wow = list()
for i in range((2*n-2)//2):
    if i%2 == 0:
        s.append(y[i]+y[2*n-2-1-i])
        s.append(y[2 * n - 2 - 1 - i] + y[i])
        s.append(y[i] + y[2 * n - 2 - 1 - 1 - i])
        s.append(y[2 * n - 2 - 1 - 1 - i] + y[i])
        s.append(y[i + 1] + y[2 * n - 2 - 1 - i])
        s.append(y[2 * n - 2 - 1 - i] + y[i + 1])
        s.append(y[i + 1] + y[2 * n - 2 - 1 - 1 - i])
        s.append(y[2 * n - 2 - 1 - 1 - i] + y[i + 1])
        for i in range(8):
            if not s[i] in dd:
                dd.update({f'{s[i]}': 1})

            else:
                dd[f'{s[i]}'] += 1
        print(dd)
        target = max(dd, key=dd.get)
        print(target)
    s.clear()