for var in range(5):
    no_classes=int(input("Enter number of classes "))
    no_attended=int(input("Enter number of attended classes "))
    per=(no_attended/no_classes)*100
    print("Your attendace percentage is ",per)
    if(per<75):
        print("Students not allowed")
    else:
        print("Students allowed")
