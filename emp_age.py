list=[]

for var in range(5):
   
    emp_id=int(input("Enter emp id "))
    name=input("Enter name ")
    age=int(input("Enter age "))
    list.append([emp_id,name,age])
    
for var2 in list:
   
    if var2[2] >50:
        print("Employee id is ",var2[0])
        print("Employee name is ",var2[1])

        
