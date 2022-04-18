t = int(input())

for _ in range(t):

    n = int(input())
    a = [int(x) for x in input().split()]

    if not sum(a) % len(a) == 0:
        print(-1)
        continue

    average = sum(a) // len(a)
    k = sum(1 for x in a if x > average)
    print(k)