number=[]

for i in range(10):
    in_number=int(input())
    number.append(in_number)
sort=sorted(number)
print("Sorted list:",sort[::-1])