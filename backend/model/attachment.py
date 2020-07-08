from enum import Enum


class Attachment(Enum):

    def get_type(self):
        _type = self.__class__.__name__
        if _type == RearGrip.__name__:
            return "Rear Grip"
        if _type == TriggerAction.__name__:
            return "Trigger Action"
        return _type


class Muzzle(Attachment):
    COLLOSUS_SUPPRESSOR = "Collosus Suppressor"
    LIGHTWEIGHT_SUPPRESSOR = "Lightweight Suppressor"
    MONOLITHIC_SUPPRESSOR = "Monolithic Suppressor"
    TACTICAL_SUPPRESSOR = "Tactical Suppressor"
    ZLR_SABRE = "ZLR Sabre"
    COMPENSATOR = "Compensator"
    MUZZLE_BRAKE = "Muzzle Brake"
    DESPERADO_PRO_COMPENSATOR = "Desperado Pro Compensator"
    FORGE_TAC_MARAUDER = "FORGE TAC Marauder"


class Barrel(Attachment):
    TEMPUS_ARCHANGEL = "Tempus 26.4\" Archangel"
    STOCK_M16_GRENADIER = "Stock M16 Grenadier"
    MONOLITHIC_INTEGRAL_SUPPRESSOR = "Monolithic Integral Suppressor"
    FSS_RECON = "FSS Recon"
    ZLR_APEX = "ZLR 16\" Apex"
    ZLR_DEADFALl = "ZLR 18\" Deadfall"
    TEMPUS_MARKSMAN = "Tempus Marksman"
    HDR_PRO = "26.9\" HDR Pro"
    FACTORY_BARREL_32 = "32.0\" Factory Barrel"
    SINGUARD_CUSTOM_276 = "Singuard Custom 27.6\""
    RPK_BARREL = "23.0\" RPK Barrel"
    STEEL = "8.7\" Steel"
    XRK_ZODIAC_S440 = "XRK Zodiac S440"
    FR_SNIPER = "FR 24.4\" Sniper"
    SINGUARD_ARMS_PROWLER = "Singuard Arms 19.8\" Prowler"
    ODEN_FACTORY_810 = "Oden Factory 810mm"
    FORGE_TAC_RETRIBUTION = "FORGE TAC Retribution"
    EXTENDED_BARREL_269 = "26.9\" Extended Barrel"
    EXTENDED_BARREL_407 = "407mm Extended Barrel"
    XRK_RANGER = "XRK Ranger"
    FACTORY_CARBINE = "16.5\" Factory Carbine"
    CORVUS_CUSTOM_MARKSMAN = "Corvus Custom Marksman"
    FSS_CARBINE_PRO = "FSS Carbine Pro"
    SINGUARD_ARMS_PRO = "Singuard Arms Pro"
    FSS_ORION = "FSS Orion"
    FSS_RANGER = "FSS Ranger"
    XRK_MARKSMAN = "XRK Marksman"
    FFS_NEXUS = "FFS 20.8\" Nexus"
    ROMANIAN = "23.0\" Romanian"
    SPETSNAZ_ELITE = "Spetsnaz Elite"
    MK3_BURST_MOD = "Mk3 Burst Mod"
    XRK_SPORT = "XRK 30.0\" Sport"
    XRK_HORIZON = "XRK Horizon 23.0\""
    STAINLESS_STEEL = "400mm Stainless Steel"
    FORGE_TAC_IMPALER = "FORGE TAC Impaler"
    LONG_BARREL = "622mm Long Barrel"


class Underbarrel(Attachment):
    COMMANDO_FOREGRIP = "Commando Foregrip"
    MERC_FOREGRIP = "Merc Foregrip"
    RANGER_FOREGRIP = "Ranger Foregrip"
    OPERATOR_FOREGRIP = "Operator Foregrip"
    STIPPLED_GRIP_TAPE = "Stippled Grip Tape"
    SNATCH_GRIP = "Snatch Grip"
    XRK_TRUEGRIP_TACTICAL = "XRK Truegrip Tactical"


class Optic(Attachment):
    VLK_3X_OPTIC = "VLK 3.0x Optic"
    VARIABLE_ZOOM_SCOPE = "Variable Zoom Scope"
    SNIPER_SCOPE = "Sniper Scope"
    VIPER_REFLEX_SIGHT = "Viper Reflex Sight"
    APX5_HOLOGRAPHIC_SIGHT = "APX5 Holographic Sight"
    GI_MINI_REFLEX = "G.I. Mini Reflex"
    CORP_COMBAT_HOLO_SIGHT = "Corp Combat Holo Sight"
    THERMAL_DUAL_POWER_SCOPE = "Thermal Dual Power Scope"
    SCOUT_COMBAT_OPTIC = "Scout Combat Optic"
    THERMAL_SNIPER_SCOPE = "Thermal Sniper Scope"
    CANTED_HYBRID = "Canted Hybrid"
    CRONEN_MINI_REFLEX = "Cronen LP945 Mini Reflex"
    FLIP_HYBRID = "4.0x Flip Hybrid"
    PBX_HOLO_SIGHT = "PBX Holo 7 Sight"


class Ammunition(Attachment):
    ROUND_MAGS_7 = "7 Round Mags"
    ROUND_MAGS_24 = "24 Round Mags"
    ROUND_DRUM_MAGS_25 = "25 Round Drum Mags"
    ROUND_MAGS_27 = "27 Round Mags"
    ROUND_MAGS_30 = "30 Round Mags"
    ROUND_DRUM_MAGS_40 = "40 Round Drum Mags"
    ROUND_MAGS_40 = "40 Round Mags"
    ROUND_MAGS_45 = "45 Round Mags"
    ROUND_MAGS_50 = "50 Round Mags"
    ROUND_MAGS_60 = "60 Round Mags"
    AUTO_30_ROUND_MAGS_10MM = "10mm Auto 30-Round Mags"
    AE_ROUND_MAGS_25 = ".41 AE 25-Round Mags"
    AE_ROUND_MAGS_32 = ".41 AE 32-Round Mags"
    BLACKOUT_MAGS = ".300 Blackout 30-Round Mags"
    NATO_ROUND_MAGS = "5.56 NATO 30-Round Mags"
    NATO_ROUND_DRUMS = "5.56 NATO 60-Round Drums"
    DRAGONS_BREATH_ROUNDS = "Dragon's Breath Rounds"
    HOLLOW_POINT = ".45 Hollow Point 12-R Mags"


class RearGrip(Attachment):
    XRK_SPEED_GRIP = "XRK Speed Grip"
    XRK_VOID_II = "XRK Void II"
    STIPPLED_GRIP_TAPE = "Stippled Grip Tape"
    RUBBERIZED_GRIP_TAPE = "Rubberized Grip Tape"
    CRONEN_SNIPER_ELITE = "Cronen Sniper Elite"


class Stock(Attachment):
    NO_STOCK = "No Stock"
    FLY_STRAP = "Fly Strap"
    FSS_CLOSE_QUARTERS_STOCK = "FSS Close Quarters Stock"
    FTAC_COLLAPSIBLE = "FTAC Collapsible"
    FTAC_CHAMPION = "FTAC Champion"
    FTAC_SPORT_COMB = "FTAC Sport Comb"
    FTAC_STALKER_SCOUT = "FTAC Stalker Scout"
    SINGUARD_ARMS_EVADER = "Singuard Arms Evader"
    SINGUARD_ARMS_ASSASSIN = "Singuard Arms Assassin"
    FORGE_TAC_CQS = "FORGE TAC CQS"
    M13_SKELETON_STOCK = "M13 Skeleton Stock"
    FTAC_XL_ELITE_COMB = "FTAC XL Elite Comb"
    SKELETON_STOCK = "Skeleton Stock"
    FORGE_TAC_CQB_COMB = "FORGE TAC CQB Comb"
    FSS_GUARDIAN = "FSS Guardian"


class Perk(Attachment):
    SLEIGHT_OF_HAND = "Sleight of Hand"
    PRESENCE_OF_MIND = "Presence of Mind"
    FMJ = "FMJ"
    FOCUS = "Focus"
    AKIMBO = "Akimbo"


class Laser(Attachment):
    TAC_LASER = "Tac Laser"
    MW_LASER_5 = "5mW Laser"


class TriggerAction(Attachment):
    LIGHTWEIGHT_TRIGGER = "Lightweight Trigger"


class Cable(Attachment):
    STRAND_CABLE_28 = "28-Strand Cable"


class Arms(Attachment):
    XRK_THUNDER_200 = "XRK Thunder 200 Lb"


class Bolt(Attachment):
    FTAC_FURY = "FTAC Fury 20\" Bolts"
