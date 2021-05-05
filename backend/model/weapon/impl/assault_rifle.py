from model.game import Game
from model.weapon.weapon import Weapon


class AssaultRifle(Weapon):
    AK_47 = "AK-47", Game.MODERN_WARFARE, ["ak"]
    AN_94 = "AN-94", Game.MODERN_WARFARE, ["an"]
    CR_56_AMAX = "CR-56 AMAX", Game.MODERN_WARFARE, ["amax", "galil"]
    FAL = "FAL", Game.MODERN_WARFARE
    FR = "FR 5.56", Game.MODERN_WARFARE, ["fr", "famas"]
    GRAU = "Grau 5.56", Game.MODERN_WARFARE, ["grau"]
    KILO_141 = "Kilo 141", Game.MODERN_WARFARE, ["kilo"]
    M4A1 = "M4A1", Game.MODERN_WARFARE, ["m4"]
    M13 = "M13", Game.MODERN_WARFARE
    ODEN = "Oden", Game.MODERN_WARFARE
    RAM_7 = "RAM-7", Game.MODERN_WARFARE, ["ram"]
    AS_VAL = "AS VAL", Game.MODERN_WARFARE, ["val"]
    SCAR = "FN Scar 17", Game.MODERN_WARFARE, ["scar"]

    XM4 = "XM4", Game.COLD_WAR
    AK_47_CW = "AK-47", Game.COLD_WAR, ["ak"]
    KRIG_6 = "Krig 6", Game.COLD_WAR, ["krig"]
    FFAR_1 = "FFAR 1", Game.COLD_WAR, ["ffar"]
    GROZA = "Groza", Game.COLD_WAR
