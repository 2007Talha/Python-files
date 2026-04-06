S=0
print("Welcome to the Quiz game !!!\n")
list=[("What is the capital of France?", "Paris"),("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),("What is the largest planet in our solar system?", "Jupiter"),("Which element has the chemical symbol 'O'?", "Oxygen"),("What is the square root of 64?", "8"),("Who painted the Mona Lisa?", "Leonardo da Vinci"),("What is the fastest land animal?", "Cheetah"),("Which country is known as the Land of the Rising Sun?", "Japan"),("What is the boiling point of water in Celsius?", "100"),("Who discovered gravity?", "Isaac Newton"),("Which is the smallest prime number?", "2"),("What is the currency of the United Kingdom?", "Pound"),("Who is known as the Father of Computers?", "Charles Babbage"),("What gas do plants absorb from the atmosphere?", "Carbon dioxide"),("Which ocean is the largest?", "Pacific Ocean"),("What is H2O commonly known as?", "Water"),("Who was the first President of the United States?", "George Washington"),("Which planet is known as the Red Planet?", "Mars"),("What is the hardest natural substance?", "Diamond"),("Which language is primarily spoken in Brazil?", "Portuguese")]
a=input("Do you want to play? YES/NO\n")
if (a=="yes" or a=="Yes" or a=="YES"):
    print("Here is your question::\n")
    forq,ans in list:
        c=str(input("ANS:")
        if c.lower()==ans:
            S=S+1
            print("YOUR ANSWER IS CORRECT YOUR SCORE IS:\n",S)
        else:
            print("X YOUR ANSWER IS WRONG YOUR SCORE IS:\n",S)
        C=input("Do you want to continue YES/NO\n")
        if (C=="no" or C=="NO" or C=="No"):
            print("GAME OVER")
            print("YOU SCORED",S,"/15")
            break
        else:
            continue
else (a=="NO" or a=="no" or a=="No"):
    break
