def cal(x):
    for b in range(1, x+1):
        for a in range(b, x + 1):
            if a % b == 0 and a * b > x and a / b < x:
                return [a, b]
    return [-1]
y = int(input())
c = cal(y)
if len(c) > 1:
    print(c[0], c[1])
else:
    print(c[0])
