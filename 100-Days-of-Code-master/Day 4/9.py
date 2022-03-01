import random 

choices = ["rock", "scissors", "paper"]
user_input = input("Enter choice: ")
r = random.choice(choices)
if user_input==r:
    print("Draw Try Again Later.")
elif user_input=="rock" and r == "scissors":
    print("You Win.")
elif user_input=="rock" and r =="paper":
    print("you lose.")
elif user_input=="paper" and r == "scissors":
    print("You Lose.")
elif user_input=="paper" and r =="rock":
    print("you win.")
elif user_input=="scissors" and r == "paper":
    print("You win.")
elif user_input=="scissors" and r =="rock":
    print("you lose.")