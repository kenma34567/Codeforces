n = int(input())
sh = str(input())
mo = str(input())
shf = 0
mof = 0
slist = []
mlist = []
for i in range(n):
    slist.append(int(sh[i]))
    mlist.append(int(mo[i]))
mlist.sort()
for i in range(n):