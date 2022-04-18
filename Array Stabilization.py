n = int(input())
x = list(map(int, input().split()))
x.sort()
if x[n-2]-x[0] < x[n-1]-x[1]:
    print(x[n-2]-x[0])
else:
    print(x[n-1]-x[1])

