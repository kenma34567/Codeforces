#from collections import OrderedDict

t = int(input())

for _ in range(t):

    n = int(input())
    a = [int(x) for x in input().split()]

    b = a.copy()
    b.sort()

    least = b[0]
    greatest = b[len(b)-1]

    least_index = a.index(least)
    greatest_index = a.index(greatest)

    #print(least_index, greatest_index)

    steps_dict = dict()
    steps_dict['least_steps'] = least_index + 1
    steps_dict['least_steps_reverse'] = len(a) - least_index
    steps_dict['greatest_steps'] = greatest_index + 1
    steps_dict['greatest_steps_reverse'] = len(a) - greatest_index

    steps_dict = {k: v for k,v in sorted(steps_dict.items(), key= lambda item: item[1])}
    #print("steps_dict", steps_dict)

    steps_key_seq = list(steps_dict)
    #print(steps_key_seq[0])

    steps = 0
    steps += steps_dict[steps_key_seq[0]]

    #print("deleted", steps_key_seq[0], steps)

    if "least_steps" == steps_key_seq[0]:

        new_starting_point = least_index
        greatest_steps = greatest_index - new_starting_point
        steps += min(greatest_steps, steps_dict['greatest_steps_reverse'])

    elif "least_steps_reverse" == steps_key_seq[0]:

        new_starting_point = least_index
        greatest_steps_reverse = new_starting_point - greatest_index
        steps += min(greatest_steps_reverse, steps_dict['greatest_steps'])

    elif "greatest_steps" == steps_key_seq[0]:

        new_starting_point = greatest_index
        least_steps = least_index - new_starting_point
        steps += min(least_steps, steps_dict['least_steps_reverse'])

    else:

        new_starting_point = greatest_index
        least_steps_reverse = new_starting_point - least_index
        steps += min(least_steps_reverse, steps_dict['least_steps'])

    print(steps)


