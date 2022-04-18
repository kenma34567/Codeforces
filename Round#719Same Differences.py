import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom



t = int(input())

for test_case in range(t):
    n = int(input())

    a = [int(num) for num in input().split()]

    diff_dict = dict()
    t = 0
    for i in range(n):

        #a[j] - j = a[i] - i

        key = a[i] - i

        if key not in diff_dict:
            diff_dict[key] = [i]
        else:
            if len(diff_dict[key]) == 1:
                diff_dict[key].append(i)
                t += 1
            else:
                t -= ncr(len(diff_dict[key]), 2)
                diff_dict[key].append(i)
                t += ncr(len(diff_dict[key]), 2)

    #print(diff_dict)
    print(t)

