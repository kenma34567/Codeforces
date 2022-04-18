t = int(input())

for test_case in range(t):

    n = int(input())

    a = []
    star_pos = []
    for i in range(n):
        a.append([[str(x) for x in line.split()] for line in input()])

    #print(a)
    for i in range(len(a)):
        line = a[i]
        for j in range(len(line)):
            if line[j][0] == "*":
                star_pos.append([i, j])
    #print(star_pos)

    first_star = star_pos[0]
    second_star = star_pos[1]

    if first_star[0] != second_star[0] and first_star[1] != second_star[1]:
        new_star_1 = [first_star[0], second_star[1]]
        new_star_2 = [second_star[0], first_star[1]]
    elif first_star[0] == second_star[0]:
        length = abs(first_star[1] - second_star[1])
        if first_star[0] + length < n:
            new_star_1 = [first_star[0] + length, first_star[1]]
            new_star_2 = [second_star[0] + length, second_star[1]]
        else:
            new_star_1 = [first_star[0] - length, first_star[1]]
            new_star_2 = [second_star[0] - length, second_star[1]]
    elif first_star[1] == second_star[1]:
        length = abs(first_star[0] - second_star[0])
        if first_star[1] + length < n:
            new_star_1 = [first_star[0], first_star[1] + length]
            new_star_2 = [second_star[0], second_star[1] + length]
        else:
            new_star_1 = [first_star[0], first_star[1] - length]
            new_star_2 = [second_star[0], second_star[1]  - length]

    #print(new_star_1, new_star_2)

    a [new_star_1[0]] [new_star_1[1]]  = ["*"]
    a [new_star_2[0]] [new_star_2[1]]  = ["*"]

    #print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j][0], end="")
        print("")

    #print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))





