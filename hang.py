import random #to generate random word
import os
import time
t=1
while(t==1):  
    from word import wordli #to get word from external module
    words=random.choice(wordli) #to get a random word
    newwo=list(words) #to make a list of letter of word
    #print(newwo)
    #print(words)
    start=time.time()
    os.system('cls')
    chance=1
    display=[]
    display.extend(newwo)
    for i in range(0,len(words)):
        display[i]='_'
        #print(display) 
    def fir(check):
        print("                          ___")
        print("                         |   0")
        print("                         |")
        print("                         |")
        print("                         |")
        print("                         |")  
        print("                         |")
    def sec(check):
        print("                          ____")
        print("                         |    0")
        print("                         |    |")
        print("                         |")
        print("                         |")
        print("                         |")  
        print("                         |")
    def thi(check):
        print("                          ____")
        print("                         |    0")
        print("                         |    |")
        print("                         |   /")
        print("                         |")
        print("                         |")  
        print("                         |")
    def fou(check):
        print("                          ____")
        print("                         |    0")
        print("                         |    |")
        print("                         |   / \ ")
        print("                         |  ")
        print("                         |")  
        print("                         |")
    def fif(check):
        print("                          ____")
        print("                         |    0")
        print("                         |    |")
        print("                         |   / \ ")
        print("                         |    |")
        print("                         |   ")  
        print("                         |")
    def six(check):
        print("                          ____")
        print("                         |    0")
        print("                         |    |")
        print("                         |   / \ ")
        print("                         |    |")
        print("                         |   /")  
        print("                         |")
        print("                         |")
    def sev(check):
        print("                              ____")
        print("                             |    0")
        print("                             |    |")
        print("                             |   / \ ")
        print("                             |    |")
        print("                             |   / \ ")  
        print("                             |")
        print("                             |")
    wo=[]
    wo.extend(newwo)
    for i in range(0,len(words)):
        wo[i]=" "
    fir(chance)
    while(chance<7 and display != newwo):
        print(" ".join(display))
        x=1
        i=0
        while(x==1):
            guess=input("Enter a letter: ")
            if guess in display:
                print("               You have already guess letter",guess.upper())
                #os.system('cls')
            elif guess in wo:
                print("               You have already guess letter",guess.upper())
                wo[i]=guess
            else:
                wo[i]=guess
                i=i+1
                x=0
        os.system('cls')
        guess=guess.lower()
        #print("chance=",chance)
        count=0
        for i in range(0,len(words)):
            if(newwo[i]==guess):
                display[i]=guess
            else:
                count=count+1
        if(count==len(words)):
            chance=chance+1
        #print(chance)        
        #print(" ".join(display))
        if(chance==1):
            fir(chance)
        elif(chance==2):
            sec(chance)
        elif(chance==3):
            thi(chance)
        elif(chance==4):
            fou(chance)
        elif(chance==5):
            fif(chance)
        elif(chance==6):
            six(chance)
        elif(chance==7):
            sev(chance)
    if(display==newwo):
        print(words.upper())
        print("You win")
    else:
        print("Sorry game over the word was",words.upper())
    end=time.time()
    times=end-start
    minu=int(times/60)
    sec=int(times%60)
    print("You take",minu, 'minutes &',sec ,' second to complete the game' )
    print("**********type '1 to play again ***or type any key to  exit")
    t=int(input("enter number: "))
    
             
     
    