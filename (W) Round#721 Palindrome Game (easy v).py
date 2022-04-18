# WRONG ANSWER

class Player:

    def __init__(self, name):
        self.name = name
        self.coin_used = 0

    def use_coin(self):
        self.coin_used += 1

def is_palindrome(s: str):
    return s == s[::-1]

def flip_to_1(player: Player, s, pos, no_of_1s):

    if s[pos] == "1":
        return s

    s_list = list(s)
    s_list[pos] = "1"
    player.use_coin()
    no_of_1s -= 1
    s = "".join(s_list)
    return s

def reverse_string(s):

    return s[::-1]


t = int(input())
for test_case in range(t):

    bob = Player("BOB")
    alice = Player("ALICE")
    turn = 0    # even: Alice, odd: Bob

    n = int(input())
    s = input()
    #print("new round", n, s)

    no_of_1s = 0
    no_of_0s = 0
    for i in range(n):

        if s[i] == "0":
            no_of_0s += 1
        elif s[i] == "1":
            no_of_1s += 1

    last_reverse = -1000

    while no_of_0s > 0:

        current_player = alice if turn % 2 == 0 else bob
        can_reverse = last_reverse != turn-1 and not is_palindrome(s)

        if can_reverse:
            #print("reversing", current_player.name, turn)
            s = reverse_string(s)
            last_reverse = turn
        else:
            preference_pos = -1
            for i in range(n):
                if s[i] == "0":
                    if preference_pos == -1:
                        preference_pos = i
                    temp_s = flip_to_1(Player("temp"), s, pos, no_of_0s)
                    if is_palindrome(temp_s):
                        preference_pos = i
                        break

            pos = preference_pos
            print("pref", s, pos)
            if pos > -1:
                s = flip_to_1(current_player, s, pos, no_of_0s)
                no_of_0s -= 1
                #print("after flipped", current_player.name, s, no_of_0s)

        turn += 1

    if no_of_0s == 0:
        result = "DRAW"
        if bob.coin_used > alice.coin_used:
            result = alice.name
        elif bob.coin_used < alice.coin_used:
            result = bob.name
        #print(bob.coin_used, alice.coin_used)
        print(result)



