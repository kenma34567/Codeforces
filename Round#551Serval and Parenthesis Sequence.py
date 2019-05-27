n = int(input())
s = str(input()[:n])
a = [0]*n
ocount = 0
ccount = 0
notfulfilled = 0
pos = 1
if n%2 !=0:
    print(":(")
else:
    for i in range(n):
        if s[i] == '(':     # 1
            a[i] = 1
            ocount += 1
        elif s[i] == ')':   # -1
            a[i] = -1
            ccount += 1
    #print(a)
    for pos in range(n-1):
        if a[pos] == 1:     # (
            notfulfilled += 1
        elif a[pos] == 0:   # ?
            #print(notfulfilled, pos)
            if ocount < n//2:
                a[pos] = 1
                ocount += 1
                notfulfilled += 1
            elif notfulfilled > 1:
                a[pos] = -1
                ccount += 1
                notfulfilled -= 1
        elif a[pos] == -1:  # )
            if notfulfilled > 1:
                notfulfilled -= 1
            else:
                print(':(')
                quit()
    #print(a)
        #print(notfulfilled)
    if a[n-1] == 1:
        print(':(')
        quit()
    else:
        a[n-1] = -1
    #print(a)
    if sum(a) == 0:
        for i in range(n):
            if a[i] == 1:
                print('(', end='')
            elif a[i] == -1:
                print(')', end='')
    else:
        print(':(')
        #print(a)