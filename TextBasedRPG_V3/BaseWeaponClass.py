# ====BASE WEAPON CLASS==== #
class BaseWeapon:                                           # ADDED A BASE WEAPON CLASS FOR WEAPONS
    # INIT
    def __init__(self , LevelRequirement , Damage):
        # STATS
        self.levelRequirement = LevelRequirement
        self.damage = Damage
        # ADD HEALTH NEXT: self.health = Health

class Stick(BaseWeapon):                                    # ADDED A STICK WEAPON CLASS
    def __init__(self):
        stickDamage = 2
        super().__init__(1 , stickDamage)