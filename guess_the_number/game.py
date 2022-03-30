from random import random


def run():

    name = input(f"First, what's your name? hehe: ")

    while name.isnumeric():

        if name.isnumeric():
            print(f"Hey, {name} isn't a name ):< ")
            name = input(f"Enter your name again (not numbers): ")

    else:

        print(f" Welcome, {name} ".center(50, '*'))

        print(f"In this game, you will guess the secret number (from 0 to 100). If you wins, you can "
              f"exit, else, you can't. ): \nOk, try it! ")

        guess = int(input(f"Enter an attempt: "))

        real = int(random() * 100)

        print(real)

        while guess != real:

            if guess > real:
                print(f"The number is less ): ")
                guess = int(input('Try again: '))
            elif guess < real:
                print(f"The number is greater ): ")
                guess = int(input(f"You can: "))
        else:

            print('You wins, hehe. See u!'.center(50, '*'))


if __name__ == '__main__':
    run()
