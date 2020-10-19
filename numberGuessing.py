import random

guesses = []

myComputer = random.randint(0,9)

player = int(input("Enter & guess the number between 0 & 9: "))
guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print("Number is too high")
    else:
        print("Number is too low")
    player = int(input("Enter & guess the number between 0 & 9: "))
    guesses.append(player)
else:
    print("you've guessed right!")
    print("it took you %i quesses " % len(guesses))
    print("these were your guesses")
    print(guesses)