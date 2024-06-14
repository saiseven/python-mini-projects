import random

top_of_range = input("enter max number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please enter a number greater than 0 next time")
        quit()
else:
    print("please type a number next time.")
    quit()

random_num=random.randint(0, top_of_range)

guesses=1
flag=0

while guesses < top_of_range:
    guesses+=1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_num:
            flag=1
            print("You got it in {} guesses!".format(guesses))
            break
        elif user_guess > random_num:
            print("Too high")
        else:
            print("Too low")
if flag==0:
    print("Better luck next time")


    
