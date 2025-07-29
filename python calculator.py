a=int(input("Enter the first no."))
b=int(input("Enter the second no."))
print("Enter the arithmetic opreration\n1.Addition\n2.subtraction\n3.multiplication\n4.division\n")
choice=int(input("Enter the choice: "))
if(choice==1):
    print(a+b)
elif(choice==2):
    print(a-b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    if(a==0):
        print("Enter valid no. to divide")
    else:
        print(a/b)
