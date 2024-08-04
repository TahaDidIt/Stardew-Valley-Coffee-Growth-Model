# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:35:31 2024

@author: Taha
"""



##### TESTING CALCULATOR
"""
Equation 1: Mnew(t) = I(t-5) - I(t-6)   OR   Mnew(t) = 4*[Mnew(t-5)]

Equation 2: M(t) = M(t-1) + Mnew(t)

Equation 3: I(t) = I(t-1) - Mnew(t) + 4*[M(t)]
"""

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