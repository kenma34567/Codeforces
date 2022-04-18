n = int(input())
s = input()
c = 0
x = 0
while c < n :
    print(s[x], end='')
    c += 1
    x += c
    if x >= len(s):
        break