#THE INTRO LINES
print("HELLO EVERYONE AND WELCOME TO THE THIRD PYTHON TUTORIAL VIDEO")
print("IN THIS VIDEO WE ARE GOING TO LEARN HOW TO MAKE A CALCULATOR USING OUR PREREQUISITE KNOWLEDGE")


#INTRO LINE
m=True
while m:
    print("hello and welcome to a built calculator")

    a= int(input("please enter the first number"))
    b = input("please enter the operation you want to perform")
    c = int(input("please enter the second number"))

    if b =="+":
        d = a+c
        print(a, "+", c, "=", d)
        

    elif b=="-":
        d = a-c
        print(a, "-", c, "=", d)

    elif b=="*":
        d = a*c
        print(a, "*", c, "=", d)

    elif b=="/":
        d = a/c
        print(a, "/", c, "=", d)
    qu = input("do you want to quite?(Y/N")
    if qu =="y" or "Y":
        m = False
    
