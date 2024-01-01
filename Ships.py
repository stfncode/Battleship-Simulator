import matplotlib
import scipy as sp
import numpy as np
from numpy import random as ran

##########################################################################################################################################################

AC = 0                                      # Define AC, so it can be referenced
INIT = []                                   # Empty Initiative Array, to be filled with the correct order of combat
A = []
B = []

##########################################################################################################################################################

"""Definition of dicerolls"""

def d6():                                   # def diceroll d6, rolls a six sided die and returns the value
    x = ran.choice([1, 2, 3, 4, 5, 6])
    return x

def d8():                                   # def diceroll d8, rolls a eight sided die and returns the value
    x = ran.choice([1, 2, 3, 4, 5, 6, 7, 8])
    return x

def d10():                                  # def diceroll d10, rolls a ten sided die and returns the value
    x = ran.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return x

def d12():                                  #def diceroll d12, rolls a twelve sided die and returns the value
    x = ran.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    return x

def d20():                                  #def diceroll d20, rolls a twenty sided die and returns the value
    x = ran.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    return x

##########################################################################################################################################################


"""Definition of all Ships"""

class Ship_A:                                # Define Class for Ship A
  Hull = 1000                                # with Hull  (100 - 1000)
  AC = 27                                    # with AC  (17 - 27)
  FP = 15                                    # with Firepower (Number of attacks per round)  (1-15?)
  SP = 4                                     # with Speed for Initiative (0-10)
  WD = 2                                     # with Wendigkeit for Initiative (0-10)
  Init = d20() + (SP + WD) // 2              # with Initiagive, calculated from SP and WD

Sp_A = Ship_A()
#print(Sp_A.Hull Sp_A.AC, Sp_A.FP)

class Ship_B:
  Hull = 1000
  AC = 27
  FP = 15
  SP = 4
  WD = 2
  Init = d20() + (SP + WD) // 2

Sp_B = Ship_B()
#print(Sp_B.Hull, Sp_B.AC, Sp_B.FP)

class Ship_C:
  Hull = 1000
  AC = 27
  FP = 15
  SP = 4
  WD = 2
  Init = d20() + (SP + WD) // 2

Sp_C = Ship_C()
#print(Sp_C.Hull, Sp_C.AC, Sp_C.FP)

class Ship_D:
  Hull = 1000
  AC = 27
  FP = 15
  SP = 4
  WD = 2
  Init = d20() + (SP + WD) // 2

Sp_D = Ship_D()
#print(Sp_D.Hull, Sp_D.AC, Sp_D.FP)

##########################################################################################################################################################

"""Create Array with all fighting Ships for Initiative!"""

SHIPS = [Ship_A.Init, Ship_B.Init, Ship_C.Init, Ship_D.Init]

##########################################################################################################################################################

"""Definition of Weapons"""

# def Light Ballista. Light Ballista is 8d6+10, +7 to hit.
def LB(AC):
    Hit = 7 + d20()                         # Attack roll
    if Hit == 27:                           # Crit Exception, always hits, double dmg dice, dmg calculation
        DMG = 10
        for i in range(16):
            x = d6()
            DMG = DMG + x
#        print("CRIT!")
    elif AC > Hit:                          # Missed Attack, 0 dmg
        DMG = 0
#        print ("Attack missed")
    else:                                   # Regular hit, dmg calculation
        DMG = 20
        for i in range(8):
            x = d6()
            DMG = DMG + x
#        print("hit")
    return DMG


# def Ballista. Ballista is 8d6+15, +8 to hit.
def BA(AC):
    Hit = 8 + d20()                         # Attack roll
    if Hit == 28:                           # Crit Exception, always hits, double dmg dice, dmg calculation
        DMG = 15
        for i in range(16):
            x = d6()
            DMG = DMG + x
#        print("CRIT!")
    elif AC > Hit:                          # Missed Attack, 0 dmg
        DMG = 0
#        print ("Attack missed")
    else:                                   # Regular hit, dmg calculation
        DMG = 20
        for i in range(8):
            x = d6()
            DMG = DMG + x
#        print("hit")
    return DMG


# def Heavy Ballista. Heavy Ballista is 8d8+15, +8 to hit.
def HB(AC):
    Hit = 8 + d20()                         # Attack roll
    if Hit == 28:                           # Crit Exception, always hits, double dmg dice, dmg calculation
        DMG = 15
        for i in range(16):
            x = d8()
            DMG = DMG + x
#        print("CRIT!")
    elif AC > Hit:                          # Missed Attack, 0 dmg
        DMG = 0
#        print ("Attack missed")
    else:                                   # Regular hit, dmg calculation
        DMG = 20
        for i in range(8):
            x = d8()
            DMG = DMG + x
#        print("hit")
    return DMG


# def Canon. Canon is 8d10+20, +9 to hit.
def CO(AC):
    Hit = 9 + d20()                         # Attack roll
    if Hit == 29:                           # Crit Exception, always hits, double dmg dice, dmg calculation
        DMG = 20
        for i in range(16):
            x = d10()
            DMG = DMG + x
#        print("CRIT!")
    elif AC > Hit:                          # Missed Attack, 0 dmg
        DMG = 0
#        print ("Attack missed")
    else:                                   # Regular hit, dmg calculation
        DMG = 20
        for i in range(8):
            x = d10()
            DMG = DMG + x
#        print("hit")
    return DMG


# def Heavy Canon. Heavy Canon is 8d12+20
def HC(AC):
    Hit = 10 + d20()
    if Hit == 30:
        DMG = 20
        for i in range(16):
            x = d12()
            DMG = DMG + x
#        print("CRIT!")
    elif AC > Hit:
        DMG = 0
#        print ("Attack missed")
    else:
        DMG = 20
        for i in range(8):
            x = d12()
            DMG = DMG + x
#        print("hit")    
    return DMG

##########################################################################################################################################################
"""                                                         2 Ship Combat!                                                                             """
##########################################################################################################################################################


"""Combat Simulation starts here"""

# Obslet Code
"""
# def Attack round of Ship 1: Ship A attacks Ship B
def Attack_A():
    HPB = Sp_B.Hull
    for i in range(Sp_A.FP):
        x = LB(Sp_B.AC)         # Change weapon here! LB, B, HB, C, HC
        HPB = HPB - x
        print (HPB)
    return HPB

# def Attack round of Ship 2: Ship B attacks Ship A
def Attack_B():
    HPA = Sp_A.Hull
    for i in range(Sp_B.FP):
        x = LB(Sp_A.AC)         # Change weapon here! LB, B, HB, C, HC
        HPA = HPA - x
        print (HPA)
    return HPA
"""


"""Combat, Ship A vs. Ship B, without Initiative!"""

def Combat():
    HPA = Sp_A.Hull
    HPB = Sp_B.Hull
    for i in range(10):                                                 # Maximum Rounds allowed
        for j in range(Sp_A.FP):
            HPB = HPB - HC(Sp_B.AC)                                     # Change Weapon of Ship A here!
#            print("Ship B has ", HPB, "HP left.")
            if HPB <= 0:
                print("Ship B has been destroyed!")
                break
        if HPB <= 0:
                print("Ship A wins the combat!")
                print("Number of Rounds: ", i+1)
                A.append("#")                                           # Track number of victories
                break    
        for j in range(Sp_B.FP):
            HPA = HPA - HC(Sp_A.AC)                                     # Change Weapon of Ship B here!
#            print("Ship A has ", HPA, "HP left.")
            if HPA <= 0:
                print("Ship A has been destroyed!")
                break
        if HPA <= 0:
                print("Ship B wins the combat!")
                print("Number of Rounds: ", i+1)
                B.append("#")                                           # Track number of victories
                break    
#        print("_________________________________")
              
##########################################################################################################################################################
        
"""Combat 2 Ships, with Initiative (simple solution)"""

def Combat_Init():
    HPA = Sp_A.Hull
    HPB = Sp_B.Hull
    Init_A = d20() + (Sp_A.SP + Sp_A.WD) // 2
    Init_B = d20() + (Sp_B.SP + Sp_B.WD) // 2
    print(Init_A, "Ship A Init")
    print(Init_B, "Ship B Init")
    if Init_A >= Init_B:
        print("Ship A moves first")
        for i in range(10):                                                 # Maximum Rounds allowed
            for j in range(Sp_A.FP):
                HPB = HPB - HC(Sp_B.AC)                                     # Change Weapon of Ship A here!
#                print("Ship B has ", HPB, "HP left.")
                if HPB <= 0:
#                    print("Ship B has been destroyed!")
                    break
            if HPB <= 0:
                    print("Ship A wins the combat!")
                    print("Number of Rounds: ", i+1)
                    A.append("#")                                           # Track number of victories
                    break    
            for j in range(Sp_B.FP):
                HPA = HPA - HC(Sp_A.AC)                                     # Change Weapon of Ship B here!
#                print("Ship A has ", HPA, "HP left.")
                if HPA <= 0:
#                    print("Ship A has been destroyed!")
                    break
            if HPA <= 0:
                    print("Ship B wins the combat!")
                    print("Number of Rounds: ", i+1)
                    B.append("#")                                           # Track number of victories
                    break    
#            print("_________________________________")
    else:
        print("Ship B moves first")
        for i in range(10):
            for j in range(Sp_B.FP):
                HPA = HPA - HC(Sp_A.AC)                                     # Change Weapon of Ship B here!
#                print("Ship A has ", HPA, "HP left.")
                if HPA <= 0:
#                    print("Ship A has been destroyed!")
                    break
            if HPA <= 0:
                    print("Ship B wins the combat!")
                    print("Number of Rounds: ", i+1)
                    B.append("#")                                           # Track number of victories
                    break      
            for j in range(Sp_A.FP):
                HPB = HPB - HC(Sp_B.AC)                                     # Change Weapon of Ship A here!
#                print("Ship B has ", HPB, "HP left.")
                if HPB <= 0:
#                    print("Ship B has been destroyed!")
                    break
            if HPB <= 0:
                    print("Ship A wins the combat!")
                    print("Number of Rounds: ", i+1)
                    A.append("#")                                           # Track number of victories
                    break            
#            print("_________________________________")
            

##########################################################################################################################################################

"""Combat 3 Ships with Initiative"""
a = d20()                                                                   # Prototype for initiative 3 ships, delete as soon as possible
#a = d4()                                                                   # replace with actual initiative from ships
b = d20()
#b = d4()
c = d20()
#c = d4()

B = [a, b, c]                                                               # Prototype Initiative Array, delete as soon as possible, replace with INIT array


C = []                                                                      # Prototype Initiative Order Array, replace with recognisable Array!



               # Initiative WORKS! 3 Ships Initiative solved!
while len(B) > 0:
    print(B)
    if a == b == c:
        C.append("a")
        B.remove(max(B))
        C.append("b")
        B.remove(max(B))
        C.append("c")
        B.remove(max(B))
    elif max(B) == a:
        C.append("a")
        B.remove(max(B))
        if a == b:
            C.append("b")
            B.remove(max(B))
        elif a == c:
            C.append("c")
            B.remove(max(B))
    elif max(B) == b:
        C.append("b")
        B.remove(max(B))
        if b == c:
            C.append("c")
            B.remove(max(B))
    else:
        C.append("c")
        B.remove(max(B))    
    print("New Array =",B)
print(C)






##########################################################################################################################################################

"""Main function starts here, test Combat!"""
# Combat() , Combat_Init()
for t in range(1000):
    Combat_Init()
print("Ship A wins", len(A), "times")
print("Ship B wins", len(B), "times")





"""Add Initiative, calculate Initiative by d20 + Wendigkeit + Speed"""

"""Add Mixed Weapons on Ship to Combat Options"""
"""Add Party vs. Multiple Ships same type"""
"""Add Party vs. Multiple Ships different type"""