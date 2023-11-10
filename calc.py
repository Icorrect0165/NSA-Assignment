print("1.For addition enter: + ","\n" "2.For subtration enter: - ","\n" "3.For multiplication enter: x ","\n" "4.For division enter: /","\n" "5.For modulus enter: %","\n" )
choice=input()
if choice=="+":
    def add():
        a =(int(input("Enter the 1st number:")))
        b =(int(input("Enter the 2nd number:")))
        c = a+b
        print (c)
    add()

elif choice=="-":
    def sub():
        a =(int(input("Enter the 1st number:")))
        b =(int(input("Enter the 2nd number:")))
        c = a-b
        print (c)
    sub()
elif choice=="x":
    def mult():
        a =(int(input("Enter the 1st number:")))
        b =(int(input("Enter the 2nd number:")))
        c = a*b
        print (c)
    mult()
elif choice=="/":
    def div():
        a =(int(input("Enter the 1st number:")))
        b =(int(input("Enter the 2nd number:")))
        c = a/b
        print (c)
    div()
elif choice=="%":
    def mod():
        a =(int(input("Enter the 1st number:")))
        b =(int(input("Enter the 2nd number:")))
        c = a%b
        print (c)
    mod()
else:
    print("Invalid Input")