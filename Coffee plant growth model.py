# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:35:31 2024

@author: Taha
"""

""" PLANNED LAYOUT:

# Setup
    imports


#functions
    2-season model
    (optional):
        testing calculator
        coffee beans to coffee revenue calculator


#Main menu
    Menu options dict
    Menu loop

"""

""" EQUATION APPENDIX:

Equation 1: V1: Mnew(t) = I(t-5) - I(t-6)

            OR
            
            V2: Mnew(t) = 4*[Mnew(t-5)]

Equation 2: M(t) = M(t-1) + Mnew(t)

Equation 3: I(t) = I(t-1) - Mnew(t) + 4*[M(t)]
"""



##### SET-UP
from datetime import datetime
import pandas as pd


##### FUNCTIONS

### Two Season model
def twoSeasonModel():
    print("__________")
    print("")
    print("")
    print("2 SEASONS MODEL:", datetime.now().strftime("%H:%M:%S"))
    print("")
    
    #starting seeds
    startSeeds = int(input("Please input number of seeds to start with: "))

    #period t=0, and list initialisation
    seedsPlanted = [startSeeds]
    I = [startSeeds]
    M = [0]
    Mnew = [0]

    #period 1 =< t < 5
    for t in range(1, 5):
        #No new plants can mature in the initial growing phase
        #And thus no new seeds can be harvested and planted from them either
        Mnew.append(0)
        M.append(0)
        seedsPlanted.append(0)
        I.append(startSeeds)
    
    #period 5 =< t < 28
    for t in range(5, 28):
        #Newly mature plants is number of seeds planted 5 periods ago
        Mnew.append(seedsPlanted[t-5])
        #Total mature is amount in previous period + newly matured
        M.append((M[t-1] + Mnew[t]))
        #Seeds planted in this period is harvest from total mature
        seedsPlanted.append((4 * M[t]))
        #Total immature is Previous period - Newly matured + Seeds planted
        I.append((I[t-1] - Mnew[t] + seedsPlanted[t]))
    
    #Output
    for t in range(0, 28):
        day = (t * 2) + 1
        totalCrops = I[t] + M[t]
        print("_____")
        print("Period t=", t, ", Day ", day)
        print("Matured today: ", Mnew[t], ", Seeds Planted: ", seedsPlanted[t])
        print("Total Crops: ", totalCrops, ", I = ", I[t], ", M = ", M[t])
        
        """ working but doesnt have a use- model into dataframe
        testdf = pd.DataFrame({"Mnew[t]": Mnew, "seedsPlanted[t]": seedsPlanted, "I[t]": I, "M[t]": M})
        """



##### OTHER FUNCTIONS



##### MAIN MENU

### Dictionary of menu functions
menuFunctions = {1: twoSeasonModel}

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