print("welcome to my computer quiz!")

playing = input("Do You want to play? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")

else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")


if answer.lower() == "random access memory":
    print("Correct!")

else:
    print("Incorrect!")

answer = input("What does VR stand for? ")


if answer.lower() == "virtual reality":
    print("Correct!")

else:
    print("Incorrect!")



