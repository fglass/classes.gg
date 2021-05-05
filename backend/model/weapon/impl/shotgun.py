from model.game import Game
from model.weapon.weapon import Weapon


class Shotgun(Weapon):
    MODEL_680 = "Model 680", Game.MODERN_WARFARE, ["model"]
    ORIGIN_12_SHOTGUN = "Origin 12 Shotgun", Game.MODERN_WARFARE, ["origin"]
    R9 = "R9-0 Shotgun", Game.MODERN_WARFARE, ["r9"]
    VLK_ROGUE = "VLK Rogue", Game.MODERN_WARFARE, ["vlk"]
