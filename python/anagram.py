from itertools import permutations

in_string=input()
permut=permutations(in_string)
for i in list(permut):
    print(''.join(list(i)))
    