n = int(input())
x = list(map(int, input().split()))
x.sort()
problem = 0
for i in range(len(x)-1):
    if i%2 == 0:
        while x[i] != x[i+1]:
            x[i] += 1
            problem += 1
print(problem)