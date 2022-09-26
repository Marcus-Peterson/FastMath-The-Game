import random
from sympy import *
import incorrect_correct as ic
from random import randint
from random import choice

correct = 0
incorrect = 0


#amt_problems = amount of problems that the player wants to solve
#Note, most of the documentations e.g comments that was written. I wrote:2022-09-21
#other comments I must have written somewhere around 2020... So bare this in mind when I'm trying 
#To explain certain functionalites in the code. This project was started around 2020

class Math_game:
    @staticmethod
    def division_game(difficulty,amt_problems):
        global correct
        global incorrect
            
        easy_mode = 1
        medium_mode = 2
        hard_mode = 3 
        #---------#---------#---------#---------#---------#---------#---------#---------
        #The code below will add 10000 division problems to three lists.
        #One for the numerator, one for denominator and one for the solution (The quotient)  
        #of the divisons
        #//2020
        #---------#---------#---------#---------#---------#---------#---------#---------
        skip_num = []                       #Numerator that is supposed to be skipped //2022-09-21
        skip_den = []                       #Denominator that is supposed to be skipped //2022-09-21
        skip_quot = []                      #Quotient that is supposed to be skipped //2022-09-21

        if difficulty == easy_mode:
            for i in range(10000):
                skip_num.append(random.randint(1,15))
                skip_den.append(random.randint(1,5))
                skip_quot.append(str(skip_num[i]/skip_den[i]))
        
        if difficulty == medium_mode:
            for i in range(10000):
                skip_num.append(random.randint(10,50))
                skip_den.append(random.randint(5,9))
                skip_quot.append(str(skip_num[i]/skip_den[i]))
        
        if difficulty == hard_mode:
            for i in range(10000):
                skip_num.append(random.randint(20,90))
                skip_den.append(random.randint(9,20))
                skip_quot.append(str(skip_num[i]/skip_den[i]))

        #---------#---------#---------#---------#---------#---------#---------#---------
        

        #---------#---------#---------#---------#---------#---------#---------#---------
        #The code below will clear all of the the division problems where there is more
        #than two decimal points. This is to get rid of division problems like:
        #"14/9 = 1.55555555556". Since the numerator & denominator is random, it's
        #nearly impossible to not have a functionality that skips these kinds of results
        #If i didn't implement the code below I would have to
        #delete both the numerator, the denominator and the dividend from the corresponding lists
        #That creates a problem: The index gets changed and will give me a: {index out of range} error 
        #If i try to call it or reference it later on in the code
        #I tried implementing something similiar in which I actually did this, I skipped all
        # of the absurd floats, but that resulted in the denominator list and numerator list
        #not accurately correspond to the dividend list. 
        # //2022-09-21
        #---------#---------#---------#---------#---------#---------#---------#---------
        div_num = []                            #The numerator that is supposed to be used # //2022-09-21
        div_den = []                            #The denominator that is supposed to be used # //2022-09-21
        div_quot = []                           #The quotient that is supposed to be used # //2022-09-21
          
        for i in range(len(skip_quot)):
            if len(skip_quot[i]) > 4:
                continue
            elif len(skip_quot[i]) <4:
                div_num.append(skip_num[i])
                div_den.append(skip_den[i])
                div_quot.append(skip_quot[i])
            elif len(div_quot) == amt_problems:
                break 
        
        c = 0
        i = 0
        while c < amt_problems:
            try:
                question = float(input(f"{div_num[i]} / {div_den[i]} = ? \n>>>"))
                if question == (float(div_quot[i])):
                    print("Correct answer!")
                    correct += 1
        
                elif question == 0:
                    print("Incorrect answer")
                    incorrect += 1
        
                elif question != (float(div_quot[i])):
                    if float(div_quot[i])==int(div_quot[i]):
                        print(f"The answer is {div_num[i]} / {div_den[i]} = {int(div_quot[i])}")
                    print("Incorrect answer")
                    print(f"The answer is {div_num[i]} / {div_den[i]} = {float(div_quot[i])}")
                    incorrect += 1
                i += 1
                c += 1
            except ValueError:
                print("Only numbers allowed")
        correct_incorrects_points()
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#---------#---------#---------#---------#---------#---------#---------#---------
#- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
#The code below describes the addition game. 
 # //2022-09-21
#---------#---------#---------#---------#---------#---------#---------#---------

    @staticmethod
    def addition_game(difficulty,amt_problems):
        
        global correct 
        global incorrect
        
        easy_mode = 1
        medium_mode = 2
        hard_mode = 3
        
        left_operator = []          
        right_operator = []
        addition_sum = []

        if difficulty == easy_mode:
            for i in range(amt_problems):
                left_operator.append(random.randint(1, 20))
                right_operator.append(random.randint(1, 20))
                addition_sum.append(left_operator[i]+right_operator[i])

        elif difficulty == medium_mode:
            for i in range(amt_problems):
                left_operator.append(random.randint(20, 40))
                right_operator.append(random.randint(20, 40))
                addition_sum.append(left_operator[i]+right_operator[i])

        elif difficulty == hard_mode:
            for i in range(amt_problems):
                left_operator.append(random.randint(40, 120))
                right_operator.append(random.randint(40, 120))
                addition_sum.append(left_operator[i]+right_operator[i])

        else:
            print("No difficulty has been chosen")
        c = 0
        i = 0
        while c < amt_problems:
            try:
                question = float(input(f"{left_operator[i]} + {right_operator[i]} = ? \n>>>"))
                if question == (float(addition_sum[i])):
                    print("Correct answer!")
                    correct += 1
        
                elif question == 0:
                    print("Incorrect answer")
                    incorrect += 1
        
                elif question != (float(addition_sum[i])):
                    print("Incorrect answer")
                    print(f"The answer is {left_operator[i]} + {right_operator[i]} = {addition_sum[i]}")
                    incorrect += 1
                i += 1
                c += 1
            except ValueError:
                print("Only numbers allowed")
        correct_incorrects_points()
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#---------#---------#---------#---------#---------#---------#---------#---------
#- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
#The code below describes the multiplication game, the variables here are more 
#self-describing  # //2022-09-21
#---------#---------#---------#---------#---------#---------#---------#---------
    @staticmethod   
    def multiplication_game(difficulty,amt_problems):
        
        global correct
        global incorrect 

        easy_mode = 1
        medium_mode = 2
        hard_mode = 3

        left_multiplication = []
        right_multiplication = []
        multiplication_product = []
        if difficulty == easy_mode:
            for i in range(amt_problems):
                left_multiplication.append(random.randint(1,10)) 
                right_multiplication.append(random.randint(1, 10))
                multiplication_product.append(left_multiplication[i]*right_multiplication[i])
            
        elif difficulty == medium_mode:
            for i in range(amt_problems):
                left_multiplication.append(random.randint(10,20)) 
                right_multiplication.append(random.randint(10, 20))
                multiplication_product.append(left_multiplication[i]*right_multiplication[i])

        elif difficulty == hard_mode:
            for i in range(amt_problems):
                left_multiplication.append(random.randint(20,60)) 
                right_multiplication.append(random.randint(20, 60))
                multiplication_product.append(left_multiplication[i]*right_multiplication[i])

        c = 0
        i = 0
        while c < amt_problems:
            try:
                question = float(input(f"{right_multiplication[i]} * {left_multiplication[i]} = ? \n>>>"))
                if question == (float(multiplication_product[i])):
                    print("Correct answer!")
                    correct += 1
        
                elif question == 0:
                    print("Incorrect answer")
                    incorrect += 1
        
                elif question != (float(multiplication_product[i])):
                    print("Incorrect answer")
                    print(f"The answer is {left_multiplication[i]} * {right_multiplication[i]} = {multiplication_product[i]}")
                    incorrect += 1
                i += 1
                c += 1
            except ValueError:
        
                print("Only numbers allowed")
        correct_incorrects_points()
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
#The code below desribes the percentage game, as with the previous problems of having absurdly long
#float() numbers, I had to implement a similiar solution to the "division-absurd-float-number-problem"
 # //2022-09-21
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#

    @staticmethod 
    def percentage_game(difficulty, amt_problems):
        global correct
        global incorrect

        #skip_percentage = []                            #The percentage solution that is supposed to be skipped
        #skip_value_left = []                            #The left value that is supposed to be skipped
        #skip_value_right = []                           ## right value that is suppposed to be skipped

        easy_mode = 1
        medium_mode = 2
        hard_mode = 3

        if difficulty == easy_mode:
            for i in range(100):
                skip_value_left.append(random.randint(1,12))
                skip_value_right.append(random.randint(1,12))
                skip_percentage.append((str(skip_value_left[i]/skip_value_right[i] *100)))
        
        if difficulty == medium_mode:
            for i in range(100):
                skip_value_left.append(random.randint(12,30))
                skip_value_right.append(random.randint(12,30))
                skip_percentage.append((str(skip_value_left[i]/skip_value_right[i] *100)))
        
        if difficulty == hard_mode:
            for i in range(100):
                skip_value_left.append(random.randint(30,70))
                skip_value_right.append(random.randint(30,70))
                skip_percentage.append((str(skip_value_left[i]/skip_value_right[i] *100)))


        percentage = []
        value_left = []
        value_right = []
        for i in range(len(skip_percentage)):
            if len(percentage) == amt_problems:
                break
    
            if float(skip_percentage[i]) % 2 == 0 or float(skip_percentage[i]) % 3 ==0 or float(skip_percentage[i]) % 4==0:
                percentage.append(skip_percentage[i])
                value_left.append(skip_value_left[i])
                value_right.append(skip_value_right[i])
        c = 0
        i = 0
        
        while c < amt_problems:
            try:
                if value_left[i] > value_right[i] and value_right[i] < value_left[i]:
                    question = float(input(f"Calculate the percentage INCREASE from {value_left[i]} => {value_right[i]}\n>>>"))
                    if question != float(percentage[i]):
                        print(f"incorrect answer, the answer is: {value_left[i]}=>{value_right[i]}=={percentage[i]}")
                        incorrect += 1
                    elif question == float(percentage[i]):
                        print("correct answer!")
                        correct += 1
            
                elif value_left[i] < value_right[i] and value_right[i] > value_left[i]:
                    question = float(input(f"Calculate the percentage DECREASE from {value_left[i]} => {value_right[i]} \n>>>"))
                    if question != float(percentage[i]):
                        print(f"incorrect answer, the answer is {value_left[i]} <= {value_right[i]} == {percentage[i]} ")
                        incorrect +=1
                    elif question == float(percentage[i]):
                        print("Correct answer!")
                        correct += 1
                elif value_left[i] == value_right[i]:
                    question = float(input(f"Calculate the percentage increase/decrease from {value_left[i]} <==> {value_right[i]} \n>>>"))
                    if question == 0: #question != float(percentage[i]):
                        print("Correct answer")                #print(f"incorrect answer! the answer is {value_left[i]} <=> {value_right[i]} == {percentage[i]}")
                        correct +=1
                    elif question == float(percentage[i]):
                        print("Correct answer!")
                        correct += 1
                i += 1
                c += 1
            except ValueError:
                print("Only numbers allowed")
        correct_incorrects_points()
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------
        #- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
        #One of the biggest hurdles I faced when making this game was the symbolic representation of algebraic formulas
        #That is where sympy came in, a library for algebra. The biggest problem was the fact that x can either
        #be a string() or a variable(). But x in of itself can not be == to an integer() or float(). Unless
        #It is stated that x is a variable that contains an int or a corresponding float that has .0 
        #but I solved it, albeit it barely. Hahaha
        # The only algebraic symbol I used was x, I wanted to include y as well. It still acheives the same thing
        #So I could never see the point of implementing that.  # //2022-09-20
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------
    @staticmethod
    def algebra_game(difficulty,amt_problems):
        global correct 
        global incorrect

        easy_mode = 1
        medium_mode = 2
        hard_mode = 3

        x = symbols("x")
        
        all_algebra = []

        if difficulty == easy_mode:
            for i in range(10000):
                all_algebra.append(Eq(random.randint(1,20) + x, random.randint(1,20)))
                

        if difficulty == medium_mode:
            for i in range(10000):
                all_algebra.append(Eq(random.randint(20,40) + x, random.randint(30,50)))
                random.shuffle(all_algebra)
                all_algebra.append(Eq(random.randint(10,40) * x, random.randint(20,50)))
        
        if difficulty == hard_mode:
            for i in range(10000):
                all_algebra.append(Eq(random.randint(40,70) + x, random.randint(50,100)))
                random.shuffle(all_algebra)
                all_algebra.append(Eq(random.randint(30,100) * x, random.randint(40,100)))


        
            
        c = 0
        i =0
        algebra_problems = []
        algebra_solutions = []
        #------------------------------------------------------------- 
                                                                    #│This piece of code was invaluable to me
        for i in range(len(all_algebra)):                           #│#Since normal ( if This == That ) equal to comparisons
            if len(algebra_problems) == amt_problems:               #│Didn't work properly with the sympy functions
                break                                               #│Becase sympy expresses the formulas with a bunch of symbols
                                                                    #│#I had to remove them so that the player doesn't get an:
            algebra_problems.append(all_algebra[i])                 #│#[incorrect answer] message when the did in fact answer correctly
            algebra_solutions.append(solve(algebra_problems[i]))    #│                                                   # //2022-09-21
            equation = str(all_algebra[i])                          #│
            equation = equation.replace(","," = ")                  #│
            equation = equation.replace("Eq","")                    #│
            equation = equation.replace("("," ")                    #│
            equation = equation.replace(")", " ")                   #│
            #--------------------------------------------------------
            
            question = (input(f"Solve for x: {equation} \n>>>"))
            if question == "" or question ==" ":
                while True:
                    print("You didn't write anything")
                    question = (input(f"Solve for x: {equation} \n>>>"))
                    if question != "" or question==" ":
                        break
            

            if question == str(algebra_solutions[i][0]) or question==str(round(algebra_solutions[i][0])) or question==algebra_solutions[i][0]:
                if  "+" in equation:
                    print("Correct answer")
                    
                    correct += 1
                
                elif len(str(algebra_solutions[i][0]))>3 and question == str(round(algebra_solutions[i][0])):
                    print('Well.. You have rounded the answer. Technically you are "correct". Whatever. Here is a half point')
                    
                    correct += 0.5
                else:
                    print("correct answer")
                    
                    correct += 1
    
            else:
                print(f"Incorrect answer:")
                print(f"x = {algebra_solutions[i][0]}")
                
                incorrect += 1
        correct_incorrects_points()
        
        
        c += 1
        i += 1
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
#The code below describes the subtraction game:
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
    @staticmethod
    def subtraction_game(difficulty,amt_problems):
        global correct
        global incorrect 
        easy_mode = 1
        medium_mode = 2
        hard_mode = 3
        

        left_subtraction = []
        right_subtraction = []
        subtraction_difference = []
        if difficulty == easy_mode:
            for i in range(amt_problems):
                left_subtraction.append(random.randint(1,10)) 
                right_subtraction.append(random.randint(1, 10))
                subtraction_difference.append(left_subtraction[i]-right_subtraction[i])
            
        elif difficulty == medium_mode:
            for i in range(amt_problems):
                left_subtraction.append(random.randint(10,20)) 
                right_subtraction.append(random.randint(2, 20))
                subtraction_difference.append(left_subtraction[i]-right_subtraction[i])

        elif difficulty == hard_mode:
            for i in range(amt_problems):
                left_subtraction.append(random.randint(10,60)) 
                right_subtraction.append(random.randint(2, 60))
                subtraction_difference.append(left_subtraction[i]-right_subtraction[i])
        c = 0
        i = 0
        
        while c < amt_problems:
            try:
                question = float(input(f"{left_subtraction[i]} - {right_subtraction[i]} = ? \n>>>"))
                if question == (float(subtraction_difference[i])):
                    if correct == 1:
                        print(f">>> {correct} point <<< ")
                    elif correct > 1:
                        print(f">>> {correct} points <<< ")
                    print("Correct answer!")
                    correct += 1
        
                elif question == 0:
                    print(f"The answer is: {left_subtraction[i]} - {right_subtraction} = {subtraction_difference[i]}")
                    print("Incorrect answer")
                    incorrect += 1
        
                elif question != (float(subtraction_difference[i])):
                    print("Incorrect answer")
                    print(f"The answer is {right_subtraction[i]} - {left_subtraction[i]} = {subtraction_difference[i]}")
                    incorrect += 1
                    
                i += 1
                c += 1
            except ValueError:
                print("You didn't write any number")
        correct_incorrects_points()
        
        
            
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
        


    
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#

#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#
#- - ↓↓↓↓↓ - -This comment-block is connected to the code below - - ↓↓↓↓↓ - -
#This is an interesting clas, this class handles the game mode: Random.
#Whenever the player chooses the random game mode, this class is called.
#One could ask why I didn't include this in the main Math_game class...
#I ask that myself. 
#If i remember correctly, I actually started this project to learn about object oriented programming back in 2020
#One of the challenges I i remember correctly was that I didn't have a good way of randomizing the output of
# The math problem and also having it correspond to how many math problems that the player wanted to solve
# So I decided it was best to put all of the functionalites of a random game in a seperate class 
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#

class Math_game_random:
    def __init__(self,difficulty,amt_problems):
        self.difficulty = difficulty
        self.amt_problems = amt_problems
        math_games_list = [Math_game.division_game, 
                      Math_game.addition_game, 
                      Math_game.multiplication_game,Math_game.algebra_game,Math_game.percentage_game,Math_game.subtraction_game]
        for _ in range(amt_problems):
            random.choice(math_games_list)(self.difficulty,1)
#---------#---------#---------#---------#---------#---------#---------#---------#---------#---------#




def correct_incorrects_points():
    
    if correct == 1 and incorrect == 1:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answer<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} correct answer<<<")
        print("-"*30)
    
    elif correct == 0 and incorrect == 0:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answers<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} correct answers<<<")
        print("-"*30)

    elif correct > 1 and incorrect > 1:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answers<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} incorrect answers<<<")
        print("-"*30)
    elif correct == 0 and incorrect > 1:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answers<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} incorrect answer<<<")
        print("-"*30)
    elif correct == 1 and incorrect == 0:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answer<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} incorrect answers<<<")
        print("-"*30)
    
    elif correct > 1 and incorrect > 1:
        print("-"*30)
        print(f"The amount of correct answers: \n>>>{correct} correct answers<<<")
        print()
        print(f"The amount of incorrect answers: \n>>>{incorrect} incorrect answers<<<")
        print("-"*30)
