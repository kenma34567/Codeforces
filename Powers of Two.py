def shift_bit_length(a):
    return 1<<(a-1).bit_length()
n, k = input().split()
n = int(n)
k = int(k)
d = 1
x = list()
if n == 0:
    print("NO")
    exit()
if n == k:
    print("YES")
    for i in range(k):
        print(1, end=' ')
    exit()
for i in range(k):
    if n > 0:
        if n - shift_bit_length(n) != 0:
            d = shift_bit_length(n)//2
        else:
            d = shift_bit_length(n)
        #print("d= " f'{d}' )
        if d == 0:
            x.append(1)
            n -= 1
        else:
            x.append(d)
            n -= d
x.sort(reverse=True)
if n > 0:
    print("NO")
    exit()
if len(x) == k:
    print("YES")
    print(*x, sep=' ')
elif len(x) > k:
    print("NO")
elif len(x) < k and x[0]//2 <= 1:
    print("NO")
else:
    p = 0
    while len(x) < k:
        if x[p] != 1:
            x.append(x[p]//2)
            x.append(x[p]//2)
            #x.sort(reverse=True)
            x.remove(x[p])
        else:
            for a in range(len(x)):
                if x[a] != 1:
                    p = a
                    break
    print("YES")
    print(*x, sep=' ')
