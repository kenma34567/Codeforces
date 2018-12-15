n = int(input())
a = [int(x) for x in input().split()]
evenness = 0
sing = 0
e = None
s = None
ex = 0
for i in range(n):
    if a[i] % 2 == 0:
        e = i+1
        evenness += 1
    if a[i] % 2 != 0:
        s = i+1
        sing += 1
    if evenness > 1 and ex != 1:
        if not s is None:
            print(s)
            ex = 1
        else:
            if a[i]%2 != 0:
                print(i+1)
                ex = 1
    elif sing > 1 and ex != 1:
        if not e is None:
            print(e)
            ex = 1
        else:
            if a[i]%2 == 0:
                print(i+1)
                ex = 1

