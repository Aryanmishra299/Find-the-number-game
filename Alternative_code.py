import random

def user():
    num = int(input("Guess the number: "))
    return num


def guess(comp, num, t):
    if comp > num:
        print(f"Your call {num} Enter the greater number")
        t += 1
        num = user()
        guess(comp, num, t)
    if comp < num:
        print(f"Your call {num} Enter the less number")
        t += 1
        num = user()
        guess(comp, num, t)
    else:
        print(f"\nYour call {num} Computer call {comp}\nYou get the number in {t} tries")

comp = random.randint(1, 50)

temp  = 1
value = user()
guess(comp, value, temp)