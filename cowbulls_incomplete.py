import random

def compare_numbers(number, user_guess):
    ## your code here
    # Initialize counts for cows and bulls
    cows = 0
    bulls = 0
    
    # Create a list to keep track of which digits have been matched
    number_list = list(number)
    user_guess_list = list(user_guess)

    # First check: Check for bulls (correct number and place)
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls += 1
            # Mark the matched digits to avoid counting them as cows
            number_list[i] = None
            user_guess_list[i] = None

    # Second check: Check for cows (correct number but wrong place)
    for digit in user_guess_list:
        if digit is not None and digit in number_list:
            cows += 1
            # Remove the matched digit from number_list to avoid double counting
            number_list[number_list.index(digit)] = None

    return (cows, bulls)  # Return a tuple of (cows, bulls)

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number // changed 0-9999 to 1000-9999 to make sure its 4 digits
guesses = 0
print number

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #raw input to input for python
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
