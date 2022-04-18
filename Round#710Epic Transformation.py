from collections import Counter
import heapq


def solve(a):
    counter_dict = Counter(a)
    h = []
    for key, value in counter_dict.items():
        heapq.heappush(h, (-value, key))

    #print("hi", len(h))
    while len(h) > 1:
        most_common = heapq.heappop(h)
        second_most_common = heapq.heappop(h)
        #print("xd", most_common, second_most_common)
        count_1 = -most_common[0]
        count_2 = -second_most_common[0]
        count_1 -= 1
        count_2 -= 1
        if count_1 > 0:
            heapq.heappush(h, (-count_1, most_common[1]))
        if count_2 > 0:
            heapq.heappush(h, (-count_2, most_common[1]))
    if len(h) > 0:
        print(-heapq.heappop(h)[0])
    else:
        print(0)


t = int(input())
for test in range(t):
    n = int(input())
    a = [int(x) for x in input().split()[:n]]
    solve(a)