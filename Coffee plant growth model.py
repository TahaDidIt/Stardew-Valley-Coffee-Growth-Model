# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:35:31 2024

@author: Taha
"""

""" PLANNED LAYOUT

# Setup
    imports



#equation functions
    eq1 V1
    eq1 V2
    eq2
    eq3



#other functions
    testing calculator
    coffee beans to coffee revenue calculator



#Main menu
    Menu options dict
    Menu loop

"""



##### SET-UP
from datetime import datetime



##### EQUATION FUNCTIONS

""" EQUATION APPENDIX:

Equation 1: V1: Mnew(t) = I(t-5) - I(t-6)

            OR
            
            V2: Mnew(t) = 4*[Mnew(t-5)]

Equation 2: M(t) = M(t-1) + Mnew(t)

Equation 3: I(t) = I(t-1) - Mnew(t) + 4*[M(t)]
"""

#Equation 1



##### OTHER FUNCTIONS



##### MAIN MENU

### Dictionary of menu functions
menuFunctions = {}

### Menu
menuChoice = ""

while menuChoice != "0":
    #Spacer with time for ease of reading
    print("")
    print("")
    print("")
    print("########## ", "Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("")
    
    #Menu choices
    print("Main Menu:")
    print("0: Exit")
    for i in menuFunctions:
        print(i, ": ", menuFunctions[i])
    
    menuChoice = input("Please select a number from the options: ")
    print("")
    
    if menuChoice == "0":
        pass
    elif int(menuChoice) in menuFunctions:
        menuFunctions[int(menuChoice)]()
    else:
        print("Invalid choice, please try again.")



"""
##### TESTING CALCULATOR

I_tminus5 = int(input("I(t-5): "))
I_tminus6 = int(input("I(t-6): "))
M_tminus1 = int(input("M(t-1): "))
I_tminus1 = int(input("I(t-1): "))

#Equation 1
Mnew_t = I_tminus5 - I_tminus6

#Equation 2
M_t = M_tminus1 + Mnew_t

#Equation 3
I_t = I_tminus1 - Mnew_t + (4*M_t)

#Output
print("__________")
print("")
print("Mnew(t): ", Mnew_t, ", M(t): ", M_t, ", I(t): ", I_t)
"""