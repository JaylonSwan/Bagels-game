import random as rand
import os
import time

debug = False
#todo
#fix save and replay ability


class data:
    NormalWins = 0
    HardWins = 0
    

class vars:
    Guesses = 0
    Guess = ""
    #Truenum is the 3 digit number you need to guess
    TrueNum = ""
    Started = False
    GameMode = "Normal"
    Win = False
    
    
def LoadData():
    SaveFile = open("Data.txt", 'r')
    Lines = SaveFile.readlines()
    
    index = 0 
    for line in Lines:
        index += 1
        if (index == 1):
            data.NormalWins = int(line.strip())
            print(line.strip())
            
        elif (index == 2):
            data.HardWins == int(line.strip())
            print(line.strip())
    SaveFile.close()
    
def SaveData(NWins, HWins):
    SaveFile = open("Data.txt", 'w')
    L = [str(NWins) + "\n", str(HWins)]
    SaveFile.writelines(L)
    SaveFile.close()

def Clear():
    os.system('cls')
    

def GetRandomNum():
   return rand.randint(1,9)
   #auto sets up the TrueNum
   
def New3DigitNum():
    while (len(vars.TrueNum) != 3):
        newnum = str(GetRandomNum())
        #dup number check
        for i in vars.TrueNum:
            if (newnum == i):
                newnum = ""
        vars.TrueNum = vars.TrueNum + newnum
    if (debug):
        print(vars.TrueNum)

def PrintStart():
    print("Welcome to Bagels Game")
    print("You will guess a random 3 digit number thats has no repeating digits")
    print("Lets Start I have a Number. You can start guessing.")
    print("---------------------------------------------------")
    print("GameMode: " + vars.GameMode)
    print(" ")
    
def RetryScreen():
    Clear()
    vars.Started = False
    if (vars.Win):
        print("--YOU WIN--")
    else:
        print("--YOU LOSE--")
    print("GameMode: " + vars.GameMode)
    print("The Number Was: " + vars.TrueNum)
    print("-------------------------------")
    
    print("1.Play Again")
    print("2.Back to Menu")
    print("--------------")
    selected = input()
    if (selected == "1"):
        vars.Started = False
        Game()
    elif (selected == "2"):
        vars.Started = False
        Menu()
    else:
        print("Input error")
    
def Game():
    if (vars.Started != True):
        New3DigitNum()
        vars.Started = True
        vars.Guesses = 1
        PrintStart()
    
    
    while (vars.Started):
        vars.Guess = input("Guess a number 0-999:")
        
        if (vars.Guesses > 0 and vars.GameMode == "Hard"):
            print("Guess #" + str(vars.Guesses))
            
        if (vars.GameMode == "Hard" and vars.Guesses >= 5):
            vars.Win = False
            RetryScreen()
            
        
        if(len(vars.Guess) != 3):
            print("Make sure that your Guess is 3 digits")
            print("Guess again")
            
            Game()
        else:
             vars.Guesses += 1
             
        # guess digits seperated and there index
        gdigits = []
        
        for i in enumerate(vars.Guess):
           gdigits.append(i[0])
           gdigits.append(i[1])
           
        index = -1
        if (vars.Guess == vars.TrueNum):
            Clear()
            vars.Win = True
            if (vars.GameMode == "Normal"):
                data.NormalWins += 1
            else:
                data.HardWins += 1
            RetryScreen()
            
        for i in vars.TrueNum:
            index += 1
            
            if (gdigits[index * 2 + 1] in vars.TrueNum):
                
                if ( gdigits[index * 2 + 1] ==  i):
                    print("FERMI")
                    
                else:
                    print("PICO")
                    
            else:
                print("BAGELS")
            
def Rules():
    Clear()
    print("--Rules--")
    print("If you guess a digit correct but it is in the wrong place i will say PICO.")
    print("If you guess a digit correct and in the rigth space i will print FERMI.")
    print("If no digit you guessed is correct i will say BAGELS.")
    print("--Rules--")
    print("type 'exit' to go back")
    selected = input()
    if (selected == "exit"):
        Menu()
    else:
        print("Input error")
        Menu()

def Menu():
    Clear()
    print(data.HardWins)
    print("----------------------")
    print("--Welocme To Bagels--")
    print("--By: Jaylon Swanson--")
    print("----------------------")
    print("1.Start")
    print("2.Rules")
    print("3.Stats")
    print("4.Exit")
    print("Type the option that you would like to select(Number)")
    print("-----------------------------------------------------")
    
    selected = input()
    
    if (selected == "1"):
        Clear()
        
        print("Select A GameMode")
        print("-------------")
        print("1.Normal")
        print("2.Hard(Only 5 Guesses)")
        print("3.Back")
        print("----------------------")
        
        selected = input()
        
        if (selected == "1"):
            vars.GameMode = "Normal"
            
            Clear()
            Game()
            
        elif (selected == "2"):
            vars.GameMode = "Hard"
            
            Clear()
            Game()
            
        elif (selected == "3"):
            Menu()
            
        else:
            print("Input error")
            time.sleep(2)
            Menu()
        
        #Game()
    elif (selected == "2"):
        Rules()
    elif (selected == "3"):
        Clear()
        print("---------")
        print("--Stats--")
        print("---------")
        print("Normal Wins:", data.NormalWins)
        print("Hard Wins:", data.HardWins)
        print("Type 'exit' to go to menu")
        if(input() =="exit"):
            Menu()
        else:
            print("Input error")
            time.sleep(2)
            Menu()
    elif (selected == "4"):
        return 
        
    else: 
        print("Input error")
        time.sleep(2)
        Menu()
        
Menu()


