import random
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def numberGuessingGame():
    user_score = 0
    score_for_correct_guess = 10
    score_for_wrong_guess = -3
    
    while(True):
        clearConsole()

        print("Enter the Game...")
        user_play_on = input("Press N to exit or, any other key to continue -> ").upper()
        if ('N' == user_play_on):
            print("Your final Score =",user_score,", See you next time!!!")
            break
                
        print("------------")
        print("Available number ranges are ->")
        print(" \
        1-10    : enter 'A' \n \
        1-20    : enter 'B' \n \
        1-50    : enter 'C' \n \
        1-100   : enter 'D' \n \
        ")

        print("------------")
        var_number_generated = 0
        user_display_list = []
        while(var_number_generated == 0):
            selection_number_range = input("Choose the range for your practice? - ").upper()
            if (selection_number_range not in ['A','B','C','D']):
                print("WARN: Please enter your choice as - A/B/C/D")
            elif ('A' == selection_number_range):
                var_number_generated = random.randint(1, 10)
            elif ('B' == selection_number_range):
                var_number_generated = random.randint(1, 20)
            elif ('C' == selection_number_range):
                var_number_generated = random.randint(1, 50)
            elif ('D' == selection_number_range):
                var_number_generated = random.randint(1, 100)
        
        print("------------")
        user_display_list.append(var_number_generated)
        user_display_list.append(var_number_generated - (random.randint(1,10)))
        user_display_list.append(var_number_generated + (random.randint(1,10)))
        random.shuffle(user_display_list)
        print("The hints for you, are -> ", user_display_list)
        
        print("------------")
        while(True):
            try:
                user_answer = int(input("Your answer is -> "))
                if (user_answer == var_number_generated):
                    user_score += score_for_correct_guess
                    print("Yayy...You WON!!!")
                else:
                    user_score += score_for_wrong_guess
                    if user_score < 0:
                        user_score = 0
                    print("Better luck next time!!!")
                print ("Current score is = ", user_score)
                break
            except ValueError:
                print("ERROR: Please enter a number from the choices")
                continue
        time.sleep(2)
        print("-/-/-/-/-/-/-/-/")

numberGuessingGame()
