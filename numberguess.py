#guess the number game
import random
t=1
while(t==1):
    n=random.randint(0,100)  
    print("Please guess the number between 1-100 ")
    print("you have 7 chance to guess")
    guess=1
    remain=7
    while(guess<8):
        print("No of guess remaning=",remain)
        number=int(input("Guess the number: "))
        if(number<n):
            print("You guess small number guess bigger") 
        elif(number>n):
            print("you guess bigger number guess smaller")

        else:

            print("you won")
            break
        guess=guess+1
        remain=remain-1

    if(guess==8):
        print("game over\n\n\n")
        print("the number was",n)
    print("**********type '1 to play again ***or type any key to  exit")
    t=int(input("enter number: "))
