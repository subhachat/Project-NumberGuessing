import random
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Score is going to be a global variable
user_score = 0

# Define few constant values
score_for_correct_guess = 10
score_for_wrong_guess = -3
range_dict = dict({'A': [1,10], 'B': [1,20], 'C': [1,50], 'D': [1,100]})

def displayRangesToUser():
    print("Available number ranges are ->")
    print(" \
    1-10    : enter 'A' \n \
    1-20    : enter 'B' \n \
    1-50    : enter 'C' \n \
    1-100   : enter 'D' \n \
    ")

def generateNumberEachRun(user_selection):
    if (user_selection not in ['A','B','C','D']):
        print("WARN: Please enter your choice as - A/B/C/D")
    else:
        minIndex = range_dict.get(user_selection)[0]
        maxIndex = range_dict.get(user_selection)[1]
        var_number_generated = random.randint(minIndex, maxIndex)
    return var_number_generated

def shuffleSequence(aList):
    random.shuffle(aList)
    return aList

def scoreCard(machine_generates, human_guess):
    global user_score
    if (human_guess == machine_generates):
        user_score += score_for_correct_guess
        print("Yayy...You WON!!!")
    else:
        user_score += score_for_wrong_guess
        if user_score < 0:
            user_score = 0
        print("Better luck next time!!!")

def numberGuessingGame():  
    while(True):
        clearConsole()

        print("Enter the Game...")
        user_play_on = input("Press N to exit or, any other key to continue -> ").upper()
        if ('N' == user_play_on):
            print("Your final Score =",user_score,", See you next time!!!")
            break
                
        print("------------")
        displayRangesToUser()        

        print("------------")
        var_number_generated = 0
        while(var_number_generated == 0):
            selection_number_range = input("Choose the range for your practice? - ").upper()
            var_number_generated = generateNumberEachRun(selection_number_range)
        
        print("------------")
        user_display_list = shuffleSequence([var_number_generated,(var_number_generated - random.randint(1,10)),(var_number_generated + random.randint(1,10))])
        print("The hints for you, are -> ", user_display_list)
        
        print("------------")
        while(True):
            try:
                user_answer = int(input("Your answer is -> "))
                scoreCard(user_answer, var_number_generated)
                print ("Your current score is = ", user_score)
                break
            except ValueError:
                print("ERROR: Please enter a number from the choices")
                continue
        time.sleep(2)
        print("-/-/-/-/-/-/-/-/")

numberGuessingGame()
