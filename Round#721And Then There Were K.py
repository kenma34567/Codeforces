t = int(input())

for test_case in range(t):
    n = int(input())
    print( ((1<<n.bit_length()-1) -1))



