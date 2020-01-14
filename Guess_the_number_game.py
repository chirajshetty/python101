import random
x = int(input("Enter the number for the range: 0 to "))
y = random.randint(0,x)
z=x+1
guess=0
while (z!=y):
    z = int(input("Guess the number:"))
    guess=guess+1
    if(z==y):
        print("You have found the number = "+str(y)+" in "+str(guess)+" guesses.")
    else:
        if(z<y):
            print("The number is higher than you expect")
        else:
            print("The number is lower than you expect")
            
