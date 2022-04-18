t = int(input())

for test_case in range(t):

    n = int(input())
    a = [int(x) for x in input().split()][:n]

    sorted_list = sorted(a)

    target = None
    if sorted_list[0] != sorted_list[1]:
        target = sorted_list[0]
    elif sorted_list[n-1] != sorted_list[n-2]:
        target = sorted_list[n-1]

    print(a.index(target)+1)
