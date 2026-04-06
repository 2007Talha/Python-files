import random
S=0
print("Welcome to the Quiz game !!!")
list=["What planet is known as the Red Planet?","What is the capital of Australia?","Who was the first President of the United States?","Who wrote Romeo and Juliet?","How many players are there in a standard football (soccer) team on the field?","What does “CPU” stand for?","Which movie features the character Jack Sparrow?","What is the largest organ in the human body?","Which language has the most native speakers worldwide?","What is the chemical symbol for gold?","What galaxy do we live in?","What is the term length of a U.S. President?","Sushi is a cuisine that originated in which country?","What is the fastest land animal?"]
a=input("Do you want to play? YES/NO")
while(a=="YES" or a=="Yes" or a=="yes"):
    n=len(list)
    b=random.randint(0,n)
    print("Here is your question::")
    print("Q:",list[b-1])
    c=str(input("Ans:"))
    if b==0:
        d= "mars"
    elif b==1:
        d= "canberra"
    elif b==2:
        d= "george wahsington"
    elif b==3:
        d= "willam shakespeare"
    elif b==4:
        d="11"
    elif b==5:
        d= "central processing unit"
    elif b==6:
        d="8"
    elif b==7:
        d= "pirates of the caribbean"
    elif b==8:
        d= "skin"
    elif b==9:
        d= "mandarin chinese"
    elif b==10:
        d= "au"
    elif b==11:
        d= "milky way"
    elif b==12:
        d= "4 years"
    elif b==13:
        d= "japan"
    elif b==14:
        d= "cheetah"
    if c.lower()==d:
        S=S+1
        print("YOUR ANSWER IS CORRECT YOUR SCORE IS:",S)
        list=list.pop(b)
    else:
        print("X YOUR ANSWER IS WRONG YOUR SCORE IS:",S)
    C=input("Do you want to continue YES/NO")
    if (C=="no" or C=="NO" or C=="No" or len(list)==0):
        print("GAME OVER")
        print("YOU SCORED",S,"/15")
        break
    else:
        continue
