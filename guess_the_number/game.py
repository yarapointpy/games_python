import random


def guess(x):

    name = input(f"First, what's your name? hehe: ")
    while name.isnumeric():

        if name.isnumeric():
            print(f"Hey, {name} isn't a name ):< ")
            name = input(f"Enter your name again (not numbers): ")

    else:

        print(f" Welcome, {name} ".center(50, '*'))

        print(f"In this game, you will guess the secret number . If you wins, you can "
              f"exit, else, you can't. ): \nOk, try it! ")

        real = random.randint(1, x)

        guess = int(input(f"Enter a number (0 - {x}): "))

        print(real)

        while guess != real:

            if guess > real:
                print(f"The number is less ): ")
                guess = int(input('Try again: '))
            elif guess < real:
                print(f"The number is greater ): ")
                guess = int(input(f"You can: "))
        else:

            print('You wins, hehe.'.center(50, '*'))


def computer_guess(x):
    print(f"Now, it's your turn :). You must tell me if i'm right or not. ")

    low = 1
    high = x
    comment = ''



    while comment != 'C':

        guess = random.randint(low, high)

        comment = input(f"Is {guess} too low (L), too high (H) or is correct (C)? D: ")
        if comment == 'L':
            guess = random.randint(guess, high)

        elif comment == 'H':
            guess = random.randint(low, guess)


    else:

        print('Yey, thanks for playing with me')



if __name__ == '__main__':
    computer_guess(500)
