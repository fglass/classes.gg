from model.game import Game
from model.weapon.weapon import Weapon


class TacticalRifle(Weapon):
    M16 = "M16", Game.COLD_WAR
    DMR = "DMR 14", Game.COLD_WAR, ["dmr"]
    TYPE_63 = "Type 63", Game.COLD_WAR, ["type"]
