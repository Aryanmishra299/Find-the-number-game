import random

computer = random.randint(1,50)
user_input = -1
guess = 0

while(user_input != computer):
    guess += 1
    user_input = int(input("Guess the number: "))
    if(user_input < computer):
        print("Your guess is too low")
    elif(user_input > computer):
        print("Your guess is too high")
        
print(f"You guessed the number in {guess} tries")
