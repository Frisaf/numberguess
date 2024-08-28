import random, time, sys

def main():
    try:
        amount_input = int(input("Type any integer bigger than 1 and press enter: "))
        if amount_input < 1:
            print("You need to type a number bigger than 1")
            main()
        
        elif amount_input == 1:
            print("Your input has to be bigger than 1.")
            main()
        
        else:
            global max_amount
            global correct_number

            max_amount = amount_input
            correct_number = random.randint(1, max_amount)

            guess()
    
    except ValueError:
        print("That is not a number. Please input an integer bigger than 1.")
        main()

def guess():
    user_guess = int(input(f"Guess a number (an integer) between 1 and {max_amount} (your input)!\n> "))

    try:
        if user_guess == correct_number:
            print(f"That's right! The correct number was {correct_number}")
            restart_question()
        
        elif user_guess > max_amount:
            print(f"Your guess has to be bigger than 1, but smaller than {max_amount}")
            guess()
        
        elif user_guess < 1:
            print(f"Your guess has to be bigger than 1, but smaller than {max_amount}")
            guess()
        
        else:
            print("Not quite! Try again!")
            guess()
    
    except ValueError:
        print("That is not a number.")
        guess()

def restart_question():
    question = input("Play again? Yes or no: ").lower()

    if question == "yes":
        print("Restarting...")
        time.sleep(2)
        main()
    
    elif question == "no":
        print("Quitting...")
        sys.exit()
    
    else:
        print("You need to answer yes or no.")
        restart_question()

main()