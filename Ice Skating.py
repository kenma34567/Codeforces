def distance(x1, x2, y1, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
n = int(input())
cor = [None] * n
for i in range(n):
    cor[i]= [int(a) for a in input().split()]
print('cor= ', cor[0])
#print('dis= ', distan
#starting_point = cor[0]ce(cor[0][0], cor[1][0], cor[0][1], cor[1][1]))
dis = [None] * (n-1)
for i in range(n-1):
    for j in range(n-1):
        if i != j:
            dis[i][j] = distance(cor[i][0], cor[j][0], cor[i][1], cor[j][1])
#for i in range(len(dis)):
    #if dis[i][j] == min(dis[i]):
        #if starting_point[0][0] != dis



"""sww = sorted(cor, key=lambda corr: corr[1])
print(sww)"""

"""dis = dict()
for i in range(n):
    dis.update({f'{cor[i]}' : distance(cor[i][0], 0, cor[i][1], 0)})
print(dis)"""
