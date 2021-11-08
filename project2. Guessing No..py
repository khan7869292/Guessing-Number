import random
randnumber=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=randnumber):
    userguess=int(input("enter your guess"))
    guesses=guesses+1
    
    if(userguess==randnumber):
        print("your guesses is right!")
    else:
        if(userguess>randnumber):
            print("your guesses is wrong! enter a smaller no.")
        else:
            print("your guesses is wrong! enter a larger no.")
  
print(f"you guessed the no. in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("you have just brokenthe high score!")

    with open("hiscore.text", "w") as f:
        f.write(str(guesses))

