# ====IMPORTS==== #
import os
from random import randint
from MyUltilities import SetCursorPos

# ====GLOBAL VARIABLES==== #
# FIXED CURSOR POSITIONS
cursorMidPosition = 38
cursorTitlePosition = 17
cursorTextPosition = 21

# ====PLAYER CLASS==== #
class Player:
    # INIT
    def __init__(self , Level , Damage , Health , Experience):
        # STATS
        self.name = "You"
        self.level = Level
        self.damage = Damage
        self.health = Health

        # EXPERIENCE POINTS
        self.experience = Experience
        self.expToLevelUp = 100

        # BOOLEAN STATES
        self.lifestate = True
        self.canEscape = True
        self.canAttack = True

        # ENEMIES
        self.enemy = None

    # SET ENEMY
    def SetEnemy(self , enemy):
        self.enemy = enemy

    # GAIN EXP ON KILL
    # UPDATE AS "player.enemy.experiencePoints" EXPERIENCE POINTS
    def GainExp(self , enemyExp):
        self.experience += enemyExp
        if self.experience >= self.expToLevelUp:
            self.experience = 0
            self.expToLevelUp += 25
            self.level += 1
        return self.experience
    
    # TAKE DAMAGE ON HIT
    # RETURN HEALTH
    # UPDATE AS "player.enemy.damage" RANDOM DAMAGE
    def TakeDamage(self , enemyDamage):
        self.health -= enemyDamage
        return self.health

#================================================#
# DISPLAY CURRENT STATS
    # DISPLAY PLAYER INFO
    def DisplayInfo(self):
        SetCursorPos(30, 2)
        print("        ")
        SetCursorPos(30, 2)
        print(self.name)
    
        SetCursorPos(30, 3)
        print("            ")
        SetCursorPos(30, 3)
        print("Level:", self.level)
    
        SetCursorPos(30, 4)
        print("              ")
        SetCursorPos(30, 4)
        print("Max Damage:", self.damage)
    
        SetCursorPos(30, 5)
        print(f"Health:" , self.health)
    
    # INSTANTLY PRINT CHOICES (VISUALS ONLY)
    def Choices(self):
        SetCursorPos(45 , cursorTextPosition)
        print("1) Attack")
        SetCursorPos(45 , cursorTextPosition+2)
        print("2) Run")

    # DISPLAY PLAYER INFO IN BATTLE
    def DisplayBattleAtr(self):
        os.system("cls")
        self.DisplayInfo()
        self.Choices()
#================================================#

# ATTACK ENEMY
    def AttackEnemy(self):
        # LOGIC
        self.canAttack = False
        enemyDamageTaken = randint(0 , self.damage)
        self.enemy.health = self.enemy.TakeDamage(enemyDamageTaken)
        SetCursorPos(60 , 8)
        if enemyDamageTaken == 0:
            print("You missed ;)")
        else:
            print("You dealt" , enemyDamageTaken , "damage.")