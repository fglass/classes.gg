from model.game import Game
from model.weapon.weapon import Weapon


class LightMachineGun(Weapon):
    HOLGER = "Holger-26", Game.MODERN_WARFARE, ["holder"]
    PKM = "PKM", Game.MODERN_WARFARE
    BRUEN = "MK9 Bruen", Game.MODERN_WARFARE, ["bruen"]
    FINN = "FiNN LMG", Game.MODERN_WARFARE, ["finn"]
    STONER_63 = "Stoner 63", Game.COLD_WAR, ["stoner"]
