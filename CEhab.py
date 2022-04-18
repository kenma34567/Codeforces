def strictly_increasing(L):
    return all(x<y for x,y in zip(L, L[1:]))
def add(L, j, x):
    for i in range(j):
        L[i] += x
    return L
def replace(L, j, x):
    for i in range(j):
        L[i] %= x
    return L
n = int(input())
a = [int(x) for x in input().split()]
count = 0
if strictly_increasing(a):
    print(0)
else:
    while not strictly_increasing(a):
        count = 0
        while count < n+1:
            for i in range(n):
                for j in range(n-i):
                    add(a, j, i+1)
                    replace(a, j, i+1)
print(a)