import random

number = random.randint(1, 10)

print("🎮 Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == number:
    print("🎉 You won! Correct!")
else:
    print("❌ Wrong!")
    print("The number was:", number)