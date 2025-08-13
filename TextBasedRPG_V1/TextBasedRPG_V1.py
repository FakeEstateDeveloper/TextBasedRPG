# ====MY OS SYSTEM==== #
# Windows 10

# ====CHATGPTED COMMANDS==== #
# 1) *** INSTANT INPUT EXECUTION ***
# import msvcrt
# print("Press any key (no Enter needed):")
# key = msvcrt.getch()  # This waits for a single keypress instantly
# print(f"You pressed: {key.decode()}")

# 2) *** OPEN CMD TERMINAL ***
# import subprocess
# import sys
# import os
# This flag makes sure we only open the new CMD window once.
# if '--new-cmd' not in sys.argv:
    # script_path = os.path.abspath(sys.argv[0])
    # cmd_command = f'start cmd /k "mode con: cols=100 lines=40 && python \"{script_path}\" --new-cmd"'
    # subprocess.run(cmd_command, shell=True)
    # sys.exit()  # Quit this instance to prevent double running

# 3) *** SET CURSOR POSITION ***
# import ctypes
# Get handle to the console output
# std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
# def set_cursor_position(x, y):
    # COORD structure expects x and y as SHORT integers packed into a single integer
    # position = (y << 16) | x
    # SetConsoleCursorPosition(handle, position)
    # ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle, position)
# Example usage:
# print("Hello at the default position")
# set_cursor_position(10, 5)  # Move cursor to column 10, row 5
# print("This is printed at x=10, y=5")

# 4) *** UNDERTALE TEXT APPEARING STYLE ***
# import time
# import sys

# def undertale_text(text, delay=0.05):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()  # Newline after the text

# # Example
# undertale_text("Hello, human. Ready for a bad time?")

#==============================================================================================#

# ====IMPORTS==== #
import subprocess
import sys
import os
import ctypes
import msvcrt
import time
from random import randint

# ====GLOBAL VARIABLES==== #
script_path = os.path.abspath(sys.argv[0])

# ====OPEN CMD TERMINAL==== #
if '--new-cmd' not in sys.argv:
    # cmd_command = f'start cmd /K "mode con: cols=100 lines=40 && python \"{script_path}\" --new-cmd"' :: k = debug , c = instant exit
    cmd_command = f'start cmd /c "mode con: cols=100 lines=40 && python \"{script_path}\" --new-cmd"'
    subprocess.run(cmd_command, shell=True)
    sys.exit()

# ====SETUP FOR CURSOR==== #
std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
def SetCursorPos(x, y):
    position = (y << 16) | x
    ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle, position)

class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_ulong),
                ("bVisible", ctypes.c_bool)]

def set_cursor_visibility(visible: bool):
    cursor_info = CONSOLE_CURSOR_INFO()
    cursor_info.dwSize = 1  # size of the cursor, 1-100
    cursor_info.bVisible = visible
    ctypes.windll.kernel32.SetConsoleCursorInfo(std_out_handle, ctypes.byref(cursor_info))
set_cursor_visibility(False) # Initialise cursor visibility to be false

#==============================================================================================#

# ====PLAYER CLASS==== #
class Player:
    def __init__(self , Level , Experience , Damage , Health):
        self.name = "You"
        self.level = Level
        self.experience = Experience
        self.damage = Damage
        self.health = Health
        self.lifestate = True       # PLAYER STARTS ALIVE
        self.canEscape = True       # PLAYER CAN ESCAPE
        self.canAttack = True       # PLAYER CAN ATTACK

    # GAIN EXP ON KILL
    def GainExp(self):
        self.experience += blueSlime.experiencePoints
        ############################################### UPDATE PLAYER EXPERIENCE TEST############################################### => SUCCESSFUL
        if self.experience >= 1:
        ############################################### UPDATE PLAYER EXPERIENCE TEST############################################### => SUCCESSFUL
            self.experience = 0
            self.level += 1
        return self.experience
    
    # TAKE DAMAGE ON HIT
    def TakeDamage(self , enemyDamage):
        self.health -= enemyDamage
        return self.health
    
    # INSTANTLY PRINT CHOICES (VISUALS ONLY)
    def Choices(self):
        SetCursorPos(45 , cursorTextPosition)
        print("1) Attack")
        SetCursorPos(45 , cursorTextPosition+2)
        print("2) Run")

    # DISPLAY PLAYER INFO
    def DisplayInfo(self):
        SetCursorPos(30, 2)
        print("        ")        # Clear line (7 spaces or more)
        SetCursorPos(30, 2)
        print(self.name)
    
        SetCursorPos(30, 3)
        print("            ")    # Clear line
        SetCursorPos(30, 3)
        print("Level:", self.level)
    
        SetCursorPos(30, 4)
        print("              ")  # Clear line
        SetCursorPos(30, 4)
        print("Max Damage:", self.damage)
    
        SetCursorPos(30, 5)
        print(f"Health:" , self.health)

    # DISPLAY PLAYER INFO IN BATTLE
    def DisplayBattleAtr(self):
        os.system("cls")
        self.DisplayInfo()
        self.Choices()

    # RANDOMIZE PLAYER DAMAGE
    def RandomSlimeDamage(self):
        return randint(0 , self.damage)

    # BATTLING BPLUE SLIME
    def BattleBlueSlimeMode(self):
        prevAttackTime = 0
        cooldownTime = 3

        self.DisplayBattleAtr()
        blueSlime.DisplayInfo()
        while blueSlime.lifestate:

            currentTime = time.time()

            if msvcrt.kbhit():
                key = msvcrt.getch()
                # GET DELTA TIME (TIME PASSED)
                if key == b"1" and self.canAttack and (currentTime - prevAttackTime>= cooldownTime):
                    prevAttackTime = currentTime
                    self.canAttack = False
                    newSlimeDamage = self.RandomSlimeDamage()
                    blueSlime.health = blueSlime.TakeDamage(newSlimeDamage)
                    SetCursorPos(60 , 8)
                    if newSlimeDamage == 0:
                        print("You missed ;)")
                    else:
                        print("You dealt" , newSlimeDamage , "damage.")

                    # ----SLIME TURN---- #
                    time.sleep(1) # WAIT BEFORE SLIME TURN
                    self.DisplayBattleAtr()
                    blueSlime.DisplayInfo()
                    result = blueSlime.AttackPlayer()
                    # SHOW RESULTS
                    if result in ("You fell to a slime...", "The slime has perished."):
                        os.system("cls")
                        print(result)
                        time.sleep(1)
                        break
                    
                    time.sleep(1)
                    self.DisplayBattleAtr()
                    blueSlime.DisplayInfo()
                    self.canAttack = True

                # ----PLAYER ESCAPE---- #
                elif key == b"2" and self.canEscape:
                    self.canEscape = False
                    chance = randint(0 , 1)
                    if chance == 1:
                        SetCursorPos(45 , cursorTextPosition-3)
                        print("You escaped :D")
                        time.sleep(1)
                        break
                    else:
                        SetCursorPos(45 , cursorTextPosition-3)
                        print("You failed to escape ;)")
                elif key == b"\x1b":    # PRESS ESC TO CLOSE TERMINAL GAME
                    os.system("cls")
                    sys.exit()

 # ----1) PLAYER---- #
player = Player(1 , 0 , 5 , 30)
# self.level        = 1
# self.experience   = 0
# self.damage       = 5
# self.health       = 30

#==============================================================================================#

# ====SLIME CLASS==== #
class Slime:
    def __init__(self , Level , ExperiencePoints , Damage , Health , Name):
        self.level = Level
        self.experiencePoints = ExperiencePoints
        self.damage = Damage
        self.health = Health
        self.name = Name
        self.lifestate = True       # SLIME STARTS ALIVE

    # SLIME TAKE DAMAGE ON HIT
    def TakeDamage(self , playerDamage):
        self.health -= playerDamage
        return self.health

    # DISPLAY SLIME INFO
    def DisplayInfo(self):
        SetCursorPos(60, 2)
        print(self.name.ljust(20))
        SetCursorPos(60, 3)
        print(f"Level: {self.level}".ljust(20))
        SetCursorPos(60, 4)
        print(f"Max Damage: {self.damage}".ljust(20))
        SetCursorPos(60, 5)
        print(f"Health: {self.health}".ljust(20))

    # PLAYER TAKE DAMAGE AND DEATHS
    def AttackPlayer(self):
        if self.health <= 0:
            self.lifestate = False

            ###############################################EXPERIENCE GAIN TEST############################################### => SUCCESSFUL
            player.GainExp()
            player.DisplayBattleAtr()
            ###############################################EXPERIENCE GAIN TEST############################################### => SUCCESSFUL

            return "The slime has perished."
        else:
            newPlayerDamageTaken = randint(0 , self.damage)
            player.TakeDamage(newPlayerDamageTaken)
            if player.health <= 0:
                player.lifestate = False
                return "You fell to a slime..."
            elif newPlayerDamageTaken == 0:
                SetCursorPos(30 , 8)
                print("The slime missed LOL")
            else:
                SetCursorPos(30 , 8)
                print("You took" , newPlayerDamageTaken , "damage.")

# ----1) BLUE SLIME---- #
blueSlime = Slime(1 , 10 , 5 , 20 , "Blue Slime")
# self.level            = 1
# self.experiencePoints = 10
# self.damage           = 5
# self.health           = 20
# ----2) PINK SLIME---- #
#pinkSlime = Slime(...)

#==============================================================================================#

# ====FUNCTIONS==== #
def CursorPrint(PrintPositionX, PrintPositionY, PrintText, Delay , Block=True):
    SetCursorPos(PrintPositionX, PrintPositionY)
    for i, char in enumerate(PrintText):
        if msvcrt.kbhit():                      # If a key was pressed
            msvcrt.getch()                      # Consume the key press
            sys.stdout.write(PrintText[i:])     # Print remaining text instantly
            sys.stdout.flush()
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Delay)
    if Block:
        while not msvcrt.kbhit():
            time.sleep(0.01)                    # Avoid CPU overuse
        msvcrt.getch()                          # Consume final key press

# ----CURSOR POSITION---- #
cursorMidPosition = 38
cursorTitlePosition = 17
cursorTextPosition = 21
# ...

# ====STATES==== #
# ...

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
player.BattleBlueSlimeMode() # SLIME ENCOUNTER AND BATTLE

# ----STAGE 2---- # :: REST
os.system("cls")
CursorPrint(40 , cursorTitlePosition , "More updates coming!" , 0.05 , True)

#++++++++++++++++++++++#
# LIST OF THINGS TO DO #
#++++++++++++++++++#+++#
# 1) OPTIMISE CODE #+++++++++++#
# 2) HIGHER LEVEL HIGHER STATS #
#++++++++++++++++++++++++++++++#

#++++++++++++++++++++++#
# FUTURE IDEAS         #
#+++++++++++++++++++++++++++++++++++++#
# 1) Undertale but hero vs demon king #
#+++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++#
# ERRORS THAT CHATGPT COULDN'T FIX  #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# player.Choices() # ERRORS MIGHT BE FROM HERE BECAUSE OF FUNCTION'S KBHIT AND GETCH #
# SOLUTION MIGHT BE JUST TO HARD CODE EXACTLY WHERE THE TEXT ARE                     #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#++++++++++++++++++++#
# ====REFLECTION==== #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# PLAN OUT AND COMMENT ALL THE FUNCTIONS NEEDED IN EACH CLASS FIRST BEFORE STARTING TO CODE #
# EVERYTHING COULD HAVE BEEN ORGANIZED BETTER                                               #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# HOW TO RUN REMINDER FOR MYSELF: cd C:\Users\dingd\OneDrive\Documents\AAAAAAAAADEVELOP\MyGames , python TextBasedRPG.py