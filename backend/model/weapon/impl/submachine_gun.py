from model.game import Game
from model.weapon.weapon import Weapon


class SubmachineGun(Weapon):
    AUG = "AUG", Game.MODERN_WARFARE
    FENNEC = "Fennec", Game.MODERN_WARFARE
    MP5 = "MP5", Game.MODERN_WARFARE
    MP7 = "MP7", Game.MODERN_WARFARE
    P90 = "P90", Game.MODERN_WARFARE
    PP19_BIZON = "PP19 Bizon", Game.MODERN_WARFARE, ["pp19", "bizon"]
    STRIKER_45 = "Striker 45", Game.MODERN_WARFARE, ["striker"]
    UZI = "Uzi", Game.MODERN_WARFARE
    ISO = "ISO", Game.MODERN_WARFARE

    MAC_10 = "MAC-10", Game.COLD_WAR, ["mac"]
    MP5_CW = "MP5", Game.COLD_WAR
    AUG_CW = "AUG", Game.COLD_WAR
    AK_74U = "AK-74u", Game.COLD_WAR, ["74", "74u"]
    BULLFROG = "Bullfrog", Game.COLD_WAR
