


def update_string(s, pos, value, quota):
    # str_list = list(s)
    # str_list[pos] = value
    s = s[:pos] + value + s[pos + 1:]
    quota -= 1
    opposite_index = opposite_pos(len(s), pos)
    if s[opposite_index] == "?" and quota > 0:
        s = s[:opposite_index] + value + s[opposite_index + 1:]
        quota -= 1

    return s, quota


def is_valid_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[opposite_pos(len(s), i)]:
            return False
        if s[i] == "?":
            return False

    return True

def opposite_pos(n, pos):
    return n - pos - 1

t = int(input())

for _ in range(t):
    # print("new")
    a, b = input().split()
    a, b = int(a), int(b)
    quota_a, quota_b = int(a), int(b)
    s = list(input())[:a + b]

    init_0 = s.count("0")
    init_1 = s.count("1")

    '''if t > 50 and _ == 39:
        print("a", a)
        print("b", b)
        print("s", s)'''

    if a < init_0 or b < init_1:
        print(-1)
        continue

    quota_a -= init_0
    quota_b -= init_1

    finish = False

    for i in range(len(s)):

        opposite_index = opposite_pos(len(s), i)
        opposite_value = s[opposite_index]

        if i == opposite_index and s[i] == "?":
            if a % 2 != 0:
                if quota_a <= 0:
                    print(-1)
                    finish = True
                    break
                s[i] = "0"
                quota_a -= 1
                #s, quota_a = update_string(s, i, "0", quota_a)
            elif b % 2 != 0:
                if quota_b <= 0:
                    print(-1)
                    finish = True
                    break
                s[i] = "1"
                quota_b -= 1
                #s, quota_b = update_string(s, i, "1", quota_b)

        elif s[i] == "?":
            if opposite_value == "0":
                if quota_a <= 0:
                    print(-1)
                    finish = True
                    break
                s[i] = "0"
                quota_a -= 1
                #s, quota_a = update_string(s, i, "0", quota_a)
            elif opposite_value == "1":
                if quota_b <= 0:
                    print(-1)
                    finish = True
                    break
                s[i] = "1"
                quota_b -= 1
                #s, quota_b = update_string(s, i, "1", quota_b)

    #print("first loop", s)

    if not finish:
        for i in range(len(s)//2 + 1):

            opposite_index = opposite_pos(len(s), i)
            opposite_value = s[opposite_index]

            if s[i] == "?" and opposite_value == "?":
                if quota_a > 0:
                    s[i] = s[opposite_index] = "0"
                    quota_a -= 2
                    #s, quota_a = update_string(s, i, "0", quota_a)
                elif quota_b > 0:
                    s[i] = s[opposite_index] = "1"
                    quota_b -= 2
                    #s, quota_b = update_string(s, i, "1", quota_b)

        #print("final", s)
        s = ''.join(s)
        if s == s[::-1] and quota_a == quota_b == 0:
            print(s)
        else:
            print(-1)


'''1
9 6
1?1??00??0??1??'''


'''
a 4
b 3
s 1?00011'''