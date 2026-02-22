import random    #impotinhg random module
comp_choice=random.randint(0,100)  #choosing range of the computer
user_guess=-1
turn=0 #calculating number of turns
while(user_guess !=comp_choice):
    turn=turn+1
    user_guess=int(input("Enter your guess"))
    if(comp_choice>user_guess):
        print("Go Higher")
    else:
        print("Go Lower")
print(f"You Got the number {comp_choice} in {turn} chances")

