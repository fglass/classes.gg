from model.game import Game
from model.weapon.weapon import Weapon


class SniperRifle(Weapon):
    AX_50 = "AX-50", Game.MODERN_WARFARE, ["ax"]
    HDR = "HDR", Game.MODERN_WARFARE
    SPR_208 = "SP-R 208", Game.MODERN_WARFARE, ["spr"]
    PELINGTON_703 = "Pelington 703", Game.COLD_WAR, ["pelington"]
