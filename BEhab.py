n, k = input().split()
n = int(n)
k = int(k)
a = []
a = list(map(int, input().split()))
try:
    a.remove(0)
except:
    a.sort()
a.sort()
for i in range(k):
    if i >= len(a):
        print("0")
    elif i == 0:
        print(a[i])
    elif (a[i] != a[i-1]):
        print(a[i]-a[i-1])
