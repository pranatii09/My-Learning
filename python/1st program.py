import random

def play_game():
    lucky_num=random.randint(1,50)
    while True:
        user_num=int(input("Guess a number between 1 and 50: "))
        if user_num==lucky_num:
            print("Congratulations! You guessed the lucky number!")
            break
        elif user_num<lucky_num:
            print("Too low! Try again.")
        else:
            print("too high! Try again.")
    print("thank you!!")

print("Welcome to the Lucky Number Game!")
print("are you ready to play? (yes/no)")
if input().lower() == "yes":
    play_game() 
else:
    print("Maybe next time! Goodbye.")
