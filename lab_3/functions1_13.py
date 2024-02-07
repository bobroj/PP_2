import random

def guess_the_number():
    # генерируем рандомное число
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print("Well,", name, ", I am thinking of a number between 1 and 20.")

    guesses_num = 0 #число попыток

    while True:
        print("Take a guess.")
        guess = int(input())

        guesses_num += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Good job,", name, "! You guessed my number in", guesses_num,  "guesses!")
            break

guess_the_number()

