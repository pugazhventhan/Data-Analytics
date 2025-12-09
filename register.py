name=["Alice","Bob","Charlie","David","Emma","Francis","Gokul","Hariharan","Raja","Karthick"]
reg_no=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510]
password=[111,112,113,114,115,116,117,118,119,120]
def registration(name, reg_no, password):
    rno = int(input("\nENTER YOUR REGISTER NUMBER: "))
    if rno in reg_no:
        i = reg_no.index(rno)
        psw = int(input("ENTER THE PASSWORD: "))
        if psw == password[i]:
            print("WELCOME", name[i])
        else:
            print("INCORRECT PASSWORD")
    else:
        print("INVALID USER ID")
        a = int(input("TO CREATE NEW ACCOUNT PRESS 1: "))
        if a == 1:
            n = input("ENTER YOUR NAME: ")
            r = int(input("CREATE YOUR REG NO: "))
            p = int(input("CREATE YOUR PASSWORD: "))
            name.append(n)
            reg_no.append(r)
            password.append(p)
            print("ACCOUNT CREATED SUCCESSFULLY!")
            registration(name, reg_no, password)
        else:
            print("EXIT")
registration(name, reg_no, password)
