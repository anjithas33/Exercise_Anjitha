class Student:
    def __init__(self, roll_no,name):
        self.roll_no=roll_no
        self.name = name

  
    # To get name
    def getData(self,rollno,name):
        print("\n")
        print("Student Details")
        print("\n")
        print("Number is  :",rollno)
        print("Name       :",name)
        
class Marks(Student):
    
    def __init__(self,mark1,mark2,mark3,mark4,mark5,mark6):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5
        self.mark6=mark6
    def getmark(self,mark1,mark2,mark3,mark4,mark5,mark6):
        tot,avg=0,0

        print("Chemistry   :",mark1)
        print("Physics     :",mark2)
        print("Maths       :",mark3)
        print("English     :",mark4)
        print("Malayalam   :",mark5)
        print("IT          :",mark6)

        tot=mark1+mark2+mark3+mark4+mark5+mark6
        average=tot/6

        print("Total marks  :",tot)
        print("Average score:",average)

stud_no=int(input("Enter studet Number: "))
stud_name=input("Enter Student name: ")

#stud = student(stud_no,stud_name)  # An Object of Person
#print("Stuednt number: ",stud.getData(stud_no))


#for i in range(6):
chem=int(input("Enter mark of chemistry:"))
phy=int(input("Enter mark of physics:"))
maths=int(input("Enter mark of maths:"))
eng=int(input("Enter mark of english:"))
mala=int(input("Enter mark of malayalam:"))
it=int(input("Enter mark of it:"))

mark=Marks(chem,phy,maths,eng,mala,it)
Marks.getData(1,stud_no,stud_name)
Marks.getmark(1,chem,phy,maths,eng,mala,it)
