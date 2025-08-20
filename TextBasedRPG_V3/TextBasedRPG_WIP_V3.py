# HOW TO RUN
# 1) Using vscode terminal, cd into the folder with all the files
# 2) Execute "python TextBasedRPG_V2" to run the game
# 3) It will open the terminal and run the game code

# ====IMPORTS==== #
import sys
import os
import time
import msvcrt
import TextColor
import EnemyClass
import BaseWeaponClass
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

# WEAPONS
# ----STICK---- #
stickWeapon = BaseWeaponClass.Stick()           # INIT NEW WEAPON STICK

#==============================================================================================#

# ====FOR TESTING==== #
# STORY CHAR APPEARING DELAY
storyDelay = 0.05

# STORY BLOCKING
storyNonBlocking = False
stodyBlocking = True                            # UPDATE TO SPAM THROUGH STORY

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
                    os.system("cls")
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
CursorPrint(cursorMidPosition , cursorTitlePosition , "Welcome To TextBasedRPG" , 0.05 , storyNonBlocking)
CursorPrint(cursorMidPosition , cursorTextPosition , "Press any key to start" , 0.05 , stodyBlocking)
os.system("cls") # CLEAR SCREEN

# ----STARTING PLOT---- #
CursorPrint(25 , cursorTitlePosition , "Hero... You are tasked to beat up the Demon King..." , 0.05 , storyNonBlocking)
CursorPrint(35 , cursorTextPosition , "Press any key to continue..." , 0.05 , stodyBlocking)
os.system("cls")

# ----STAGE 1---- # :: SLIME BATTLE
CursorPrint(25 , cursorTitlePosition , "You begin your journey through the Forest of Desolation." , 0.05 , storyNonBlocking)
CursorPrint(35 , cursorTextPosition , "Press any key to continue..." , 0.05)
os.system("cls")
CursorPrint(31 , cursorTitlePosition , "You have encountered a LVL 1 Slime!" , 0.05 , storyNonBlocking)
CursorPrint(40 , cursorTextPosition , "What will you do?" , 0.05 , stodyBlocking)
os.system("cls")
# BLUE SLIME ENCOUNTER AND BATTLE
# INIT
# ----1ST BATTLE---- # :: BLUE_SLIME
playerInstance.SetWeapon(stickWeapon)           # SET PLAYER'S WEAPON AS "STICK"
playerInstance.SetEnemy(blueSlimeInstance)      # playerInstance."" TO ACCESS STATS
blueSlimeInstance.SetEnemy(playerInstance)      # blueSlimeInstance."" TO ACCESS STATS
BattleEncounter(blueSlimeInstance , playerInstance)
os.system("cls")

# ----STAGE 2---- # :: REST                     # VERY VERY TERRIBLE ISSUE: IF PLAYER SPAMS BUTTONS A LOT AFTER BATTLE ENDS SKIPS ALL STORY DIALOGUE
if not playerInstance.canEscape:
    playerInstance.canEscape = True
else:
    CursorPrint(cursorMidPosition , cursorTitlePosition , "After defeating the slime," , 0.05 , storyNonBlocking)
    CursorPrint(42 , cursorTextPosition , f"{TextColor.Color.red}you got stronger...{TextColor.Color.reset}" , 0.1 , stodyBlocking)
    os.system("cls")
    CursorPrint(cursorMidPosition , cursorTitlePosition , "However, you just murdered" , 0.05 , storyNonBlocking)
    CursorPrint(cursorMidPosition , cursorTextPosition , "an innocent slime that was" , 0.05 , stodyBlocking)
    os.system("cls")
    CursorPrint(35 , 14 , f"{TextColor.Color.red}just minding its own business...{TextColor.Color.reset}" , 0.15 , stodyBlocking)
    os.system("cls")

# ----STAGE 3---- # ::
CursorPrint(cursorMidPosition-4 , cursorTitlePosition , "You continue walking down the path" , 0.05 , storyNonBlocking)                # ADDED MORE TEXT CONTENT
CursorPrint(cursorMidPosition-4 , cursorTextPosition , "until you stumble upon a shiny object..." , 0.05 , stodyBlocking)
os.system("cls")

# ----MORE UPDATES COMING---- #
os.system("cls")
CursorPrint(40 , cursorTitlePosition , "More updates coming!" , 0.05 , stodyBlocking)