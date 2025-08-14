# HOW TO RUN
# 1) Using vscode terminal, cd into the folder with all the files
# 2) Execute "python TextBasedRPG_V2" to run the game
# 3) It will open the terminal and run the game code

# ====IMPORTS==== #
import sys
import os
import time
import msvcrt
import EnemyClass
from random import randint
from PlayerClass import Player
from MyUltilities import SetCursorPos

# FIXED CURSOR POSITIONS
cursorMidPosition = 38
cursorTitlePosition = 17
cursorTextPosition = 21

# HEROS
# ----DEFAULT HERO---- #
playerInstance = Player(1 , 5 , 30 , 0) # level , damage , health , experience

# ENEMIES
# ----BLUE SLIME---- #
blueSlimeInstance = EnemyClass.BlueSlime()

#==============================================================================================#

# ====FUNCTIONS==== #
# CURSOR PRINT
def CursorPrint(PrintPositionX, PrintPositionY, PrintText, Delay , Block=True):
    SetCursorPos(PrintPositionX, PrintPositionY)
    for i, char in enumerate(PrintText):
        if msvcrt.kbhit():
            msvcrt.getch()
            sys.stdout.write(PrintText[i:])     # PRINT REMAINING TEXT INSTANTLY
            sys.stdout.flush()
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Delay)
    if Block:
        while not msvcrt.kbhit():
            time.sleep(0.01)                    # AVOID OVERUSING CPU
        msvcrt.getch()                          # CONSUME FINAL KEYPRESS

# BATTLE ENCOUNTER
# SCALABLE BATTLE CODE

def BattleEncounter(enemyInstance , playerInstance):
    # DELTA TIME
    prevAttackTime = 0
    cooldownTime = 3

    # DISPLAY INFORMATION
    playerInstance.DisplayBattleAtr()
    enemyInstance.DisplayInfo()

    # BATTLE LOOP
    while enemyInstance.lifestate and playerInstance.lifestate:
        currentTime = time.time()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"1" and playerInstance.canAttack and (currentTime - prevAttackTime>= cooldownTime):
                prevAttackTime = currentTime

                # PLAYER TURN
                playerInstance.AttackEnemy()

                # CLEAR PLAYER DMAGE TO SLIME
                time.sleep(0.75)
                playerInstance.DisplayBattleAtr()
                enemyInstance.DisplayInfo()

                # SLIME TURN
                enemyInstance.AttackPlayer()
                
                # SHOW
                time.sleep(0.75)
                playerInstance.DisplayBattleAtr()
                enemyInstance.DisplayInfo()
                playerInstance.canAttack = True

            # PRESS 2 TO ESCAPE (50% CHANCE)
            elif key == b"2" and playerInstance.canEscape:
                playerInstance.canEscape = False
                chance = randint(0 , 1)
                if chance == 1:
                    SetCursorPos(45 , cursorTextPosition-3)
                    print("You escaped :D")
                    time.sleep(1)
                    break
                else:
                    SetCursorPos(45 , cursorTextPosition-3)
                    print("You failed to escape ;)")

            # PRESS ESC TO CLOSE TERMINAL GAME
            elif key == b"\x1b":
                os.system("cls")
                sys.exit()

#==============================================================================================#

# ====ENTRY POINT==== #
# ----LORE---- #
# The hero goes on a journey to beat up the demon king
# But why? What did the demon king do? Is it because he is a demon?
# Racism? Are humans just racist?

# ---TITLE SCREEN---- #
CursorPrint(cursorMidPosition , cursorTitlePosition , "Welcome To TextBasedRPG" , 0.05 , False)
CursorPrint(cursorMidPosition , cursorTextPosition , "Press any key to start" , 0.05)
os.system("cls") # CLEAR SCREEN

# ----STARTING PLOT---- #
CursorPrint(25 , cursorTitlePosition , "Hero... You are tasked to beat up the Doraemon King..." , 0.05 , False)
CursorPrint(35 , cursorTextPosition , "Press any key to continue..." , 0.05)
os.system("cls")

# ----STAGE 1---- # :: SLIME BATTLE
CursorPrint(25 , cursorTitlePosition , "You begin your journey through the Forest of Desolation." , 0.05 , False)
CursorPrint(35 , cursorTextPosition , "Press any key to continue..." , 0.05)
os.system("cls")
CursorPrint(31 , cursorTitlePosition , "You have encountered a LVL 1 Slime!" , 0.05 , False)
CursorPrint(40 , cursorTextPosition , "What will you do?" , 0.05 , True)
os.system("cls")
# BLUE SLIME ENCOUNTER AND BATTLE
# INIT
# ----1ST BATTLE---- #
playerInstance.SetEnemy(blueSlimeInstance)      # playerInstance."" TO ACCESS STATS
blueSlimeInstance.SetEnemy(playerInstance)      # blueSlimeInstance."" TO ACCESS STATS
BattleEncounter(blueSlimeInstance , playerInstance)

# ----STAGE 2---- # :: REST
os.system("cls")
CursorPrint(40 , cursorTitlePosition , "More updates coming!" , 0.05 , True)

# FUTURE IDEAS
# 1) ADD A NEW MONSTER... WHAT COULD IT BE? ;)
# 2) RANDOMISE BATTLE ENCOUNTERS
# 3) COMPILE MY GAME INTO AN EXE FILE
