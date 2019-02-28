n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
a = [int(x) for x in input().split()]
b = a.copy()
a.sort(reverse=True)
sp = sum(a[0:m*k])
temp = a[0:m*k]
start = 0
print(sp)
t = 0   #count elements in one subarray
c = 0   #count no. of subarray
temp2 = dict()
for i in range(len(temp)):
    if temp[i] in temp2:
        temp2[temp[i]] += 1
    else:
        temp2[temp[i]] = 1
for i in range(n):
    if b[i] in temp2 and temp2[b[i]] > 0:
        t += 1
        temp2[b[i]] -= 1
    if t == m and i-start>=m-1:
        print(i+1, end=' ')
        start = i+1
        t = 0
        c += 1
        if c == k-1:
            break