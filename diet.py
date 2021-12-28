#daily diet and exercise management system
# import datetime
# def datetime():
#     return datetime.datetime.now()
def  writes(b):
    if(b==1):
        exercise=input("enter the exercise ")
        with open("exercise.txt","a") as f:
            f.write(str(exercise))
            print(" ")
    else:
        diet=input("\nenter the diet") 
        with open("diet.txt","a") as f:
            f.write("\n",diet) 
def  read(c):
    if(c==1):
        with open("exercise.txt") as f:
            for i in f:
                print(i)
     
    else:
        with open("diet.txt") as f:
            for i in f:
                print(i)
         


a=int(input("Enter '1' for write data and '2' for read data"))
if(a==1):
    b=int(input(" Enter '1' for exercise and '2' for dite"))
    writes(b)
elif(a==2):
    c=int(input("Enter '1' for exercise and '2' for dite to read data"))
    read(c)
else:
    print("invalid input")