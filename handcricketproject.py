import random
score1=0
score2=0
def bat(): 
    #b is comp and bu is user
    def ufirstin():
        global score1    
        while(1):
            b=random.randint(1,6)
            while(1):
                bu=int(input("enter "+name+"'s choice 1-6:"))
                if(bu>=1 and bu<=6):
                    break
                else:
                    print("in valid input enter correct choice")
            print("computers choice",b)
            if b==bu:
                print(name,"'s choice:",bu,sep="")
              
                print(name,", is out",sep="")
                print(name,"'s score:",score1,sep="")
                break
            else:
                score1=score1+bu
                print("score=",score1)
        usecondin(score1)      
    def usecondin(sc):
        global score2
        print("second innings starts")
        print("target for computer is:",score1+1)
        while(score2<=score1+1):
            bw=random.randint(1,6)
            while(1):
                bwu=int(input("enter "+name+"'s choice 1-6:"))
                if(bwu>=1 and bwu<=6):
                    break
                else:
                    print("in valid input enter correct choice")
            print("computer opted for:",bw)
            if bw==bwu:      
                print("computer is out")
                print("comp score:",score2)
                break
            else:
                score2=score2+bw
                print("computer score is:",score2)
                d1=sc-score2
                if(d1>0):
                    print("computer needs",d1+1,"runs to win")
        if (score1==score2):
            print("match draw")
        elif(score2>score1):
            print("computer won")
        else:
            print(name,"you won the match")
    ufirstin()
def bowl():
    #b is comp and bu is user
    def ufirstin():
        global score1
        while(1):
            b=random.randint(1,6)
            while(1):
                bu=int(input("enter "+name+"'s choice 1-6:"))
                if(bu>=1 and bu<=6):
                    break
                else:
                    print("in valid input enter correct choice")
            print("computers choice:",b)
            if b==bu:
                print(name,"'s choice:",bu,sep="")
                print("computer is out")
                print("computer total score:",score1)
                break
            else:
                score1=score1+b
                print(" Total score=",score1)
        usecondin(score1)
    def usecondin(sc):
        global score2
        print("second innings starts")
        print("target for user is:",score1+1)
        while(score2<=score1+1):
            bw=random.randint(1,6)
            while(1):
                bwu=int(input("enter "+name+"'s choice 1-6:"))
                if(bwu>=1 and bwu<=6):
                    break
                else:
                    print("in valid input enter correct choice")
            print("computer opted for:",bw)
            if bw==bwu:  
                print(name," is out",sep="")
                print(name,"'s score:",score2,sep="")
                break
            else:
                score2=score2+bwu
                print(name,"'s score is:",score2,sep="")
                d1=sc-score2
                if(d1>0):
                    print("user needs",d1+1,"runs to win")
        if (score1==score2):
            print("match draw")
                
        elif(score2>score1):
            print(name,"won the match....... ")     
        else:
            print("computer won")
    ufirstin()
name=input("Enter Name:")
print("WELCOME",name,"TO HANDCRICKET GAME")
print("you will have 1 wicket")
print("Its Toss Time")                   #t is computer and tu is user
while(1):
    ch=input("choose Even or Odd(e/o):")
    if(ch=='e' or ch=='o'):
        break
    else:
        print("invalid input  please enter correct input")
t=random.randint(1,6)
while(1):
    tu=int(input("enter number from 1 to 6:"))
    if(tu>=1 and tu<=6):
        break
    else:
        print("invalid input please enter again")
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
