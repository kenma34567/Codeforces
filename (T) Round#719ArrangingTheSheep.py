#TLEEEEEE

def is_sheep(s):
    return "*" == s

def find_nth_sheep(s, n):
    #print("finding nth sheep", n)
    sheep = "*"
    sheep_pos = s.find(sheep)
    while sheep_pos >= 0 and n > 1:
        sheep_pos = s.find(sheep, sheep_pos+1)
        n -= 1
    return sheep_pos

def move_sheep(s, lock_sheep_pos, no_of_sheep, move_count):

    for i in range(len(s)):
        if is_sheep(s[i]):
            if i < lock_sheep_pos and not is_sheep(s[i+1]):
                #print("pos[" + str(i) + "] should go right", move_count)
                s = go_right(s, i)
                move_count += 1
            elif i > lock_sheep_pos and not is_sheep(s[i-1]):
                #print("pos[" + str(i) + "] should go left", move_count)
                s = go_left(s, i)
                move_count += 1
    #print("after", s)
    #print("c", move_count)
    if not is_grouped(s, no_of_sheep):
        move_count = move_sheep(s, lock_sheep_pos, no_of_sheep, move_count)

    return move_count

def go_right(s, i):
    str_list = list(s)
    str_list[i], str_list[i+1] = str_list[i+1], str_list[i]
    return "".join(str_list)

def go_left(s, i):
    str_list = list(s)
    str_list[i], str_list[i-1] = str_list[i-1], str_list[i]
    return "".join(str_list)

def is_grouped(s, no_of_sheep):
    if no_of_sheep <= 1:
        return True
    first_group_end = -1
    disconnect = False
    for i, c in enumerate(s):

        if first_group_end > -1:
            if not is_sheep(c):
                #print("disconnected at", i)
                disconnect = True

        if is_sheep(c):
            first_group_end = i
            if disconnect:
                return False

    return True


t = int(input())

for test_case in range(t):
    n = int(input())
    s = input()
    no_of_sheep = s.count("*")
    lock_sheep_pos = find_nth_sheep(s, int(no_of_sheep/2) + (no_of_sheep%2 > 0))
    #print(lock_sheep_pos)
    move_count = 0
    move_count = move_sheep(s, lock_sheep_pos, no_of_sheep, move_count)
    #print("fin", move_count)
    print(move_count)

