#This code was written 2022-09-19 & debugged, fixed and finally implemented in 2022-09
import random
from game_functions import *
import time

class Main_class():
    @staticmethod
    def start_game():
        
        print("press 1 for random\n press 2 for addition\n press 3 for subtraction\n")
        print("press 4 for multiplication\n press 5 for percentage\n press 6 for algebra\n")
        print("press 7 for division")
        while True:
            try:
                user_select_game_mode = int(input("Choose the math game-mode\n>>>"))
                if user_select_game_mode in list(range(1,8)):
                    break
                
                elif user_select_game_mode not in list(range(1,8)):
                    print("Only numbers between 1 & 6 allowed")
                    continue
            except ValueError:
                print("Only NUMBERS between 1 & 6 allowed")
                continue
        

        
        while True:
            try:
                user_select_difficulty = int(input("Select diffcutly\n \n1=Easy Mode\n \n2=Medium Mode\n \n3=Hard mode\n \n>>>"))
                if user_select_difficulty in list(range(1,4)):
                    break
                
                elif user_select_difficulty not in list(range(1,4)):
                    print("only numbers between 1 & 3 allowed")
                    continue
            except ValueError:
                print("Only NUMBERs between 1 & 3 allowed")

        while True:
            try:
                user_select_amount_math_problems = int(input("Select the amount of problems\n>>>"))
                
                if user_select_amount_math_problems >= 100:
                    try:
                        sanity_check = input(f"Really... Do you REALLY want {user_select_amount_math_problems} mathematical problems\n>>>")
                        print("Type yes or no")
                        if sanity_check == "yes":
                            break
                        elif sanity_check == "no" or "No" or "NO" or "nO":
                            continue

                    except ValueError:
                        print("Types yes or no")
                        
                elif user_select_amount_math_problems <= 100:
                    print("Time to start")
                    from alive_progress import alive_bar
                    def compute():
                        for i in range(10000):
                            #...  process items as usual.
                            yield  # to mark tha an item has been processed
                    
                    with alive_bar(10000) as bar:
                        for i in compute():
                            bar()
                    break

            except ValueError:
                print("Only NUMBERS allowed")
        U_S_D = user_select_difficulty                #The difficulty settings of the game
        S_A_M_P = user_select_amount_math_problems     #Selected amount of problems that the player wants to solve
        
        math_games_dict = {1:lambda:Math_game_random(U_S_D,S_A_M_P),
                           
                           2:lambda:Math_game.addition_game(U_S_D,S_A_M_P),

                           3:lambda:Math_game.subtraction_game(U_S_D,S_A_M_P),

                           4:lambda:Math_game.multiplication_game(U_S_D,S_A_M_P),

                           5:lambda:Math_game.percentage_game(U_S_D,S_A_M_P),

                           6:lambda:Math_game.algebra_game(U_S_D,S_A_M_P),

                           7:lambda:Math_game.division_game(U_S_D,S_A_M_P),}
        def final_start():
            start = math_games_dict[user_select_game_mode]
            start()
                
        final_start()
        
        #print(":", list(math_games_dict.keys())
        #[list(math_games_dict.values()).index(selected_mode)])
        
    


Main_class.start_game()
        


    

    
    
    

