# ====IMPORTS==== #
# from random import randint
import os
from random import randint
from time import sleep
from MyUltilities import SetCursorPos

# ====GLOBAL VARIABLES==== #
# FIXED CURSOR POSITIONS
cursorMidPosition = 38
cursorTitlePosition = 17
cursorTextPosition = 21

# ====ENEMY CLASS==== #
class Enemy:
    def __init__(self , Name , Level , Damage , Health , ExperiencePoints):
        # STATS
        self.name = Name
        self.level = Level
        self.damage = Damage
        self.health = Health
        self.experiencePoints = ExperiencePoints
        

# ====SLIME CLASS==== #
class BlueSlime(Enemy):
    def __init__(self):
        # STATS
        super().__init__("Blue Slime" , 1 , 5 , 20 , 50)

        # BOOLEAN STATES
        self.lifestate = True

        # PLAYER
        self.enemy = None

    # SET PLAYER
    def SetEnemy(self, enemy):
        self.enemy = enemy

    # SLIME TAKE DAMAGE ON HIT
    # RETURN HEALTH
    # UPDATE AS "player.damage" RANDOM DAMAGE
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

    def AttackPlayer(self):
        # WAIT BEFORE SLIME TURN
        sleep(1)

        # LOGIC
        # SLIME DAMAGE TAKEN
        if self.health <= 0:
            self.lifestate = False
            self.enemy.GainExp(self.experiencePoints)
            self.enemy.DisplayBattleAtr()
            os.system("cls")
            SetCursorPos(cursorMidPosition , cursorTitlePosition)
            print("Of course the slime died...")
            sleep(1) # SHOW RESULTS FOR 1 SEC
            return True
        # PLAYER DAMAGE TAKEN
        else:
            playerDamageTaken = randint(0 , self.damage)
            self.enemy.TakeDamage(playerDamageTaken)
            if self.enemy.health <= 0:
                self.enemy.lifestate = False
                os.system("cls")
                SetCursorPos(cursorMidPosition , cursorTitlePosition)
                print("You died to a slime LMAO")
                sleep(1) # SHOW RESULTS FOR 1 SEC
                return True
            # IF STILL ALIVE AFTER HIT
            elif playerDamageTaken == 0:
                SetCursorPos(30 , 8)
                print("The slime somehow missed????")
            else:
                SetCursorPos(30 , 8)
                print("You took" , playerDamageTaken , "damage.")