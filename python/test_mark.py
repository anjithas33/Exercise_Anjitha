marks=[]
#least=[]
sum_mrk,avg=0,0

print("Enter scores")
for i in range(10):
    mark=int(input())
    marks.append(mark)
#print(marks)

for i in marks:
    if i > 100 or i <0 :
        print("Some avlues are wrong! Please check score")

sum_mrk=sum(marks)
avg=sum_mrk/10

print("Lowest score : ",min(marks)) 
print("Highest score: ",max(marks)) 
print("Average is   : ",round(avg))

sort_mark=sorted(marks)
#print(sort_mark)

#second largest score
print("second largest score: ",sort_mark[-2])

sort_mark.pop(0)
sort_mark.pop(0)

new_avg=sum(sort_mark)/8
print("New average    :",round(new_avg))