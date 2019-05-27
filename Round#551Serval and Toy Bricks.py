length, width, height = [int(x) for x in input().split()]
#print(length, width, height)
front = [int(x) for x in input().split()[:width]]
#print(front)
#print()
left = [int(x) for x in input().split()[:length]]
a = list()
for i in range(length):
    a = [int(x) for x in input().split()]
    for j in range(width):
        if a[j] == 1:
            a[j] = front[j] # front
        if a[j] > 0 and left[i] < a[j]:
            a[j] = left[i]  # left
    a = [str(x) for x in a]
    print(' '.join(a))