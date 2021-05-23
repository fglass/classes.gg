from enum import Enum
from model.game import Game
from model.weapon.weapon_data_loader import WEAPON_DATA


class Weapon(Enum):
    def __init__(self, name: str, game: Game, aliases: list = None):
        self._name = name
        self._game = game
        self._aliases = aliases if aliases else []

    def __str__(self):
        return self._name

    @property
    def game(self) -> Game:
        return self._game

    @property
    def aliases(self) -> list:
        return [self._name.lower()] + self._aliases

    @property
    def attachments(self) -> list:
        return WEAPON_DATA[self.name] if self.name in WEAPON_DATA else []


class AssaultRifle(Weapon):
    AK_47 = "AK-47", Game.MODERN_WARFARE, ["ak", "ak47"]
    AN_94 = "AN-94", Game.MODERN_WARFARE, ["an94"]
    CR_56_AMAX = "CR-56 AMAX", Game.MODERN_WARFARE, ["amax", "cr56", "galil"]
    FAL = "FAL", Game.MODERN_WARFARE
    FR = "FR 5.56", Game.MODERN_WARFARE, ["famas", "fr"]
    GRAU = "Grau 5.56", Game.MODERN_WARFARE, ["grau"]
    KILO_141 = "Kilo 141", Game.MODERN_WARFARE, ["kilo"]
    M4A1 = "M4A1", Game.MODERN_WARFARE, ["m4"]
    M13 = "M13", Game.MODERN_WARFARE
    ODEN = "Oden", Game.MODERN_WARFARE
    RAM_7 = "RAM-7", Game.MODERN_WARFARE, ["ram"]
    AS_VAL = "AS VAL", Game.MODERN_WARFARE, ["val"]
    SCAR = "FN Scar 17", Game.MODERN_WARFARE, ["scar"]

    AK_47_CW = "AK-47", Game.COLD_WAR, ["ak", "ak47"]
    FARA = "FARA 83", Game.COLD_WAR, ["fara"]
    FFAR_1 = "FFAR 1", Game.COLD_WAR, ["ffar"]
    GROZA = "Groza", Game.COLD_WAR
    KRIG_6 = "Krig 6", Game.COLD_WAR, ["krig"]
    QBZ = "QBZ-83", Game.COLD_WAR, ["qbz"]
    XM4 = "XM4", Game.COLD_WAR


class SubmachineGun(Weapon):
    AUG = "AUG", Game.MODERN_WARFARE
    FENNEC = "Fennec", Game.MODERN_WARFARE, ["vector"]
    MP5 = "MP5", Game.MODERN_WARFARE
    MP7 = "MP7", Game.MODERN_WARFARE
    P90 = "P90", Game.MODERN_WARFARE, ["p-90"]
    PP19_BIZON = "PP19 Bizon", Game.MODERN_WARFARE, ["bizon", "pp19"]
    STRIKER_45 = "Striker 45", Game.MODERN_WARFARE, ["striker"]
    UZI = "Uzi", Game.MODERN_WARFARE
    ISO = "ISO", Game.MODERN_WARFARE

    AK_74U = "AK-74u", Game.COLD_WAR, ["74", "74u"]
    BULLFROG = "Bullfrog", Game.COLD_WAR
    KSP_45 = "KSP 45", Game.COLD_WAR, ["ksp"]
    LC10 = "LC10", Game.COLD_WAR, ["lc"]
    MAC_10 = "MAC-10", Game.COLD_WAR, ["mac"]
    MILANO_821 = "Milano 821", Game.COLD_WAR, ["milano"]
    MP5_CW = "MP5", Game.COLD_WAR
    PPSH = "PPSH-41", Game.COLD_WAR, ["ppsh"]


class LightMachineGun(Weapon):
    BRUEN = "MK9 Bruen", Game.MODERN_WARFARE, ["bruen"]
    FINN = "FiNN LMG", Game.MODERN_WARFARE, ["finn"]
    HOLGER = "Holger-26", Game.MODERN_WARFARE, ["holder"]
    M60 = "M60", Game.COLD_WAR
    M91 = "M91", Game.MODERN_WARFARE
    MG34 = "MG35", Game.MODERN_WARFARE, ["mg"]
    PKM = "PKM", Game.MODERN_WARFARE
    RPD = "RPD", Game.COLD_WAR
    SA87 = "SA87", Game.MODERN_WARFARE
    STONER_63 = "Stoner 63", Game.COLD_WAR, ["stoner"]


class SniperRifle(Weapon):
    AX_50 = "AX-50", Game.MODERN_WARFARE, ["ax"]
    DRAGUNOV = "Dragunov", Game.MODERN_WARFARE
    HDR = "HDR", Game.MODERN_WARFARE
    PELINGTON_703 = "Pelington 703", Game.COLD_WAR, ["pelington"]
    RYTEC_AMR = "Rytec AMR", Game.MODERN_WARFARE, ["rytec"]


class MarksmanRifle(Weapon):
    CROSSBOW = "Crossbow", Game.MODERN_WARFARE, ["cbow"]
    EBR = "EBR-14", Game.MODERN_WARFARE, ["ebr"]
    KAR98K = "Kar98k", Game.MODERN_WARFARE, ["kar"]
    MK2_CARBINE = "MK2 Carbine", Game.MODERN_WARFARE, ["mk2", "carbine"]
    SKS = "SKS", Game.MODERN_WARFARE
    SPR_208 = "SP-R 208", Game.MODERN_WARFARE, ["spr", "sp-r"]


class TacticalRifle(Weapon):
    AUG_CW = "AUG", Game.COLD_WAR
    CARV = "CARV.2", Game.COLD_WAR, ["carv"]
    M16 = "M16", Game.COLD_WAR
    DMR = "DMR 14", Game.COLD_WAR, ["dmr"]
    TYPE_63 = "Type 63", Game.COLD_WAR, ["type"]


class Shotgun(Weapon):
    MODEL_680 = "Model 680", Game.MODERN_WARFARE, ["model"]
    ORIGIN_12_SHOTGUN = "Origin 12 Shotgun", Game.MODERN_WARFARE, ["origin"]
    R9 = "R9-0 Shotgun", Game.MODERN_WARFARE, ["r9"]
    VLK_ROGUE = "VLK Rogue", Game.MODERN_WARFARE, ["vlk"]


class Handgun(Weapon):
    DIAMATTI = "Diamatti", Game.COLD_WAR
    M19 = "M19", Game.MODERN_WARFARE
    RENETTI = "Renetti", Game.MODERN_WARFARE
    SYKOV = "Sykov", Game.MODERN_WARFARE
