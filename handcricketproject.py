import random
def bat():
    score1=0
    #b is comp and bu is user
    def ufirstin():
        b=random.randint(1,6)
        bu=int(input("enter your choice 1-6:"))
        if b==bu:
            print("user choosed:",bu)
            print("computer opted for this:",b)
            print("you are out")
            print("user score:",score1)
        else:
            print("you scored:",bu)
            score1=score1+bu
            print("score=",score1)
        return(score1)
        usecondin(score1)
    def usecondin(sc):
        score2=0
        print("second innings starts")
        print("target for computer is:",score1+1)
        bw=random.randint(1,6)
        bwu=int(input("enter your choice 1-6:"))
        if bw==bwu:
            print("computer opted for:",bw)
            print("computer is out")
            print("comp score:",score2)
            if (score1==score2):
                print("match draw")
            elif(score2>score1):
                print("computer won")
            else:
                print("user won")
        else:
            print("computer scored:",bw)
            score2=score2+bw
            print("computer score is:",score2)
            d1=sc-score2
            if(d1>0):
                print("computer needs",d1+1,"runs to win")
def bowl():
    score1=0
    #b is comp and bu is user
    def ufirstin():
        b=random.randint(1,6)
        bu=int(input("enter your choice 1-6:"))
        if b==bu:
            print("user choice:",bu)
            print("computer opted for this:",b)
            print("computer is out")
            print("computer score:",score1)
        else:
            print("computer scored:",b)
            score1=score1+b
            print("score=",score1)
        return(score1)
        usecondin(score1)
    def usecondin(sc):
        score2=0
        print("second innings starts")
        print("target for user is:",score1+1)
        bw=random.randint(1,6)
        bwu=int(input("enter your choice 1-6:"))
        if bw==bwu:
            print("computer opted for:",bw)
            print("your are out")
            print("user score:",score2)
            if (score1==score2):
                print("match draw")
                
            elif(score2>score1):
                print("user won")
                
            else:
                print("computer won")
        else:
            print(" you scored:",bwu)
            print("computer choose:",bw)
            score2=score2+bwu
            print("user score is:",score2)
            d1=sc-score2
            if(d1>0):
                print("user needs",d1+1,"runs to win")

name=input("Enter Name:")
print("WELCOME",name,"TO HANDCRICKET GAME")
print("you will have 1 wicket")
print("Its Toss Time")
#t is computer and tu is user
ch=input("choose Even or Odd(e/o):")
t=random.randint(1,6)
tu=int(input("enter number from 1 to 6:"))
toss=t+tu
print("computer choice is:",t)
if(toss%2==0):
    if(ch=='e'):
        print("you won the toss")
        u=1
    else:
        print("you loss the toss")
        u=0
else:
    if(ch=='o'):
        print("you won the toss")
        u=1
    else:
        print("you loss the toss")
        u=0
if(u==1):
    d=int(input("1.bat or 2.bowl?(1/2):"))
    if(d==1):
        print("you choosed bat first")
        bat()
    else:
        print("you choosed to bowl first")
        bowl()
else:
    d=random.randint(1,2)
    if(d==1):
        print("computer choose to bat first")
        bowl()
    else:
        print("computer choose to bowl first")
        bat()
