list_student=["ali","ahmad","ahad","hamza"]
v1=0
v2=0
for var in list_student:
    print("Enter record for ",var)
    no_classes=int(input("Enter number of classes "))
    no_attended=int(input("Enter number of attended classes "))
    per=(no_attended/no_classes)*100
    print("Your attendace percentage is ",per)
    if(per<75):
        print("Students not allowed")
        v1=v1+1
    else:
        print("Students allowed")
        v2=v2+1
print("Total number of students allow",v1)
print("Total number of students allow",v2)
        
