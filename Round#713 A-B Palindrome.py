def opposite_pos(n, pos):
    return n - pos - 1


def update_string(s, pos, value, quota):
    # str_list = list(s)
    # str_list[pos] = value
    s = s[:pos] + value + s[pos + 1:]
    quota -= 1
    if s[opposite_pos(len(s), pos)] == "?" and quota > 0:
        s = s[:opposite_pos(len(s), pos)] + value + s[opposite_pos(len(s), pos) + 1:]
        quota -= 1

    return s, quota


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[opposite_pos(len(s), i)]:
            return False

    return True


t = int(input())

for _ in range(t):
    # print("new")
    a, b = input().split()
    a, b = int(a), int(b)
    quota_a, quota_b = int(a), int(b)
    s = input()[:a + b]

    unknown_pos = []
    unknown_pos2 = []
    init_0 = s.count("0")
    init_1 = s.count("1")

    if a < init_0 or b < init_1:
        print(-1)
        continue

    quota_a -= init_0
    quota_b -= init_1

    for i in range(len(s)):
        if s[i] == "?":
            unknown_pos.append(i)

    finish = False

    for i in unknown_pos:

        if s[i] != "?":
            continue

        should_recheck = True

        opposite_value = s[opposite_pos(len(s), i)]
        if opposite_value == "1":
            if quota_b <= 0:
                print(-1)
                finish = True
                break
            s, quota_b = update_string(s, i, "1", quota_b)
            should_recheck = False
        elif opposite_value == "0":
            if quota_a <= 0:
                print(-1)
                finish = True
                break
            s, quota_a = update_string(s, i, "0", quota_a)
            should_recheck = False

        if should_recheck:
            unknown_pos2.append(i)

    if not finish:
        for i in unknown_pos2:
            if s[i] != "?":
                continue

            if opposite_pos(len(s), i) == i:
                if a % 2 != 0:
                    s, quota_a = update_string(s, i, "0", quota_a)
                elif b % 2 != 0:
                    s, quota_b = update_string(s, i, "1", quota_b)
            else:
                opposite_value = s[opposite_pos(len(s), i)]
                if opposite_value == "?":
                    if quota_a < quota_b:
                        if quota_b <= 0:
                            print(-1)
                            finish = True
                            break
                        s, quota_b = update_string(s, i, "1", quota_b)
                    elif quota_a >= quota_b:
                        if a <= 0:
                            print(-1)
                            finish = True
                            break
                        s, quota_a = update_string(s, i, "0", quota_a)
            # print("checlk", s, quota_a, quota_b)

        if not is_palindrome(s):
            print(-1)
        else:
            print(s)


            '''1
9 6
1?1??00??0??1??'''