from enum import Enum

from model.game import Game


class Weapon(Enum):

    def __init__(self, name, game=Game.MODERN_WARFARE):
        self._name = name
        self._game = game

    def __str__(self):
        return self._name

    # Assault rifle
    AK_47 = "AK-47"
    AN_94 = "AN-94"
    CR_56_AMAX = "CR-56 AMAX"
    FAL = "FAL"
    FAMAS = "FR 5.56"
    GRAU = "Grau 5.56"
    KILO_141 = "Kilo 141"
    M4A1 = "M4A1"
    M13 = "M13"
    ODEN = "Oden"
    RAM_7 = "RAM-7"
    AS_VAL = "AS VAL"
    XM4 = "XM4", Game.COLD_WAR
    AK_47_CW = "AK-47 CW", Game.COLD_WAR
    KRIG_6 = "Krig 6", Game.COLD_WAR
    FFAR_1 = "FFAR 1", Game.COLD_WAR
    GROZA = "Groza", Game.COLD_WAR

    # Tactical Rifles
    M16 = "M16", Game.COLD_WAR
    DMR = "DMR 14", Game.COLD_WAR
    TYPE_63 = "Type 63", Game.COLD_WAR

    # LMG
    HOLGER = "Holger-26"
    PKM = "PKM"
    BRUEN = "MK9 Bruen"
    STONER_63 = "Stoner 63", Game.COLD_WAR

    # SMG
    AUG = "AUG"
    FENNEC = "Fennec"
    MP5 = "MP5"
    MP7 = "MP7"
    P90 = "P90"
    PP19_BIZON = "PP19 Bizon"
    STRIKER_45 = "Striker 45"
    UZI = "Uzi"
    MAC_10 = "MAC-10", Game.COLD_WAR
    MP5_CW = "MP5 CW", Game.COLD_WAR
    AK_74U = "AK-74u", Game.COLD_WAR

    # Sniper rifle
    AX_50 = "AX-50"
    HDR = "HDR"
    SPR_208 = "SP-R 208"
    PELINGTON_703 = "Pelington 703", Game.COLD_WAR

    # Marksman rifle
    KAR98K = "Kar98k"
    CROSSBOW = "Crossbow"

    # Shotgun
    MODEL_680 = "Model 680"
    ORIGIN_12_SHOTGUN = "Origin 12 Shotgun"
    R9 = "R9-0 Shotgun"
    VLK_ROGUE = "VLK Rogue"

    # Pistol
    M19 = "M19"
    RENETTI = "Renetti"
    DIAMATTI = "Diamatti", Game.COLD_WAR
