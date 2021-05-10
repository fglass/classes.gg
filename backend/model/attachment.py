from enum import Enum

from model.game import Game


@DeprecationWarning
class Attachment(Enum):

    def __init__(self, name, game=Game.MODERN_WARFARE, aliases: list = None):
        self._name = name
        self._game = game
        self._aliases = aliases if aliases else []

    def __str__(self):
        return self._name

    @property
    def aliases(self) -> list:
        return [self._name.lower()] + self._aliases

    @classmethod
    def get_class_name(cls):
        _type = cls.__name__
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
    CHOKE = "Choke"
    FLASH_GUARD = "Flash Guard"

    INFANTRY_COMPENSATOR = "Infantry Compensator", Game.COLD_WAR
    SUPPRESSOR = "Suppressor", Game.COLD_WAR
    AGENCY_SUPPRESSOR = "Agency Suppressor", Game.COLD_WAR
    KGB_ELIMINATOR = "KGB Eliminator", Game.COLD_WAR
    SPETSNAZ_COMPENSATOR = "Spetsnaz Compensator", Game.COLD_WAR
    STABILIZER = "Stabilizer .308", Game.COLD_WAR
    MUZZLE_BRAKE_545 = "Muzzle Brake 5.45", Game.COLD_WAR
    MUZZLE_BRAKE_556 = "Muzzle Brake 5.56", Game.COLD_WAR
    MUZZLE_BRAKE_762 = "Muzzle Brake 7.62", Game.COLD_WAR
    MUZZLE_BRAKE_9 = "Muzzle Brake 9", Game.COLD_WAR
    GRU_SILENCER = "GRU Silencer", Game.COLD_WAR
    SOCOM_ELIMINATOR = "SOCOM Eliminator", Game.COLD_WAR
    GRU_SUPPRESSOR = "GRU Suppressor", Game.COLD_WAR


class Barrel(Attachment):
    TEMPUS_ARCHANGEL = "Tempus 26.4\" Archangel"
    STOCK_M16_GRENADIER = "Stock M16 Grenadier"
    MONOLITHIC_INTEGRAL_SUPPRESSOR = "Monolithic Integral Suppressor"
    FSS_RECON = "FSS Recon"
    ZLR_APEX = "ZLR 16\" Apex"
    ZLR_DEADFALL = "ZLR 18\" Deadfall"
    TEMPUS_MARKSMAN = "Tempus Marksman"
    HDR_PRO = "26.9\" HDR Pro"
    FACTORY_BARREL_32 = "32.0\" Factory Barrel"
    SINGUARD_CUSTOM_276 = "Singuard Custom 27.6\""
    RPK_BARREL = "23.0\" RPK Barrel"
    STEEL = "8.7\" Steel"
    XRK_ZODIAC_S440 = "XRK Zodiac S440"
    XRK_EQUINOX_S440 = "XRK Equinox S440"
    FR_SNIPER = "FR 24.4\" Sniper"
    SINGUARD_ARMS_PROWLER = "Singuard Arms 19.8\" Prowler", Game.MODERN_WARFARE, ["singuard 19.8"]
    SINGUARD_ARMS_SOCOM = "Singuard Arms 16.6\" SOCOM"
    SINGUARD_ARMS_WHISPER = "Singuard Arms Whisper"
    ODEN_FACTORY_810 = "Oden Factory 810mm"
    FORGE_TAC_RETRIBUTION = "FORGE TAC Retribution"
    EXTENDED_BARREL_269 = "26.9\" Extended Barrel"
    EXTENDED_BARREL_407 = "407mm Extended Barrel"
    LIGHTWEIGHT_407 = "407mm Lightweight"
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
    MK1_EXTENDED = "Mk1 Extended"
    MK3_BURST_MOD = "Mk3 Burst Mod"
    XRK_SPORT = "XRK 30.0\" Sport"
    XRK_HORIZON = "XRK Horizon 23.0\""
    STAINLESS_STEEL = "400mm Stainless Steel"
    FORGE_TAC_IMPALER = "FORGE TAC Impaler"
    FORGE_TAC_PRECISION = "FORGE TAC Precision"
    FORGE_TAC_SENTRY = "FORGE TAC Sentry"
    FORGE_TAC_LB = "FORGE TAC 17.2\" LB"
    LONG_BARREL = "622mm Long Barrel"
    XRK_SUMMIT = "XRK Summit 26.8\""
    OSW_PARA = "13.0\" OSW Para"
    ULTRALIGHT_179 = "17.9\" Ultralight"
    ULTRALIGHT_18 = "18.0\" Ultralight"
    AN_FACTORY = "AN-94 Factory X-438mm"
    XRK_208_DRAGOON = "XRK 208 Dragoon"
    VLK_200 = "VLK 200mm Osa"
    SPR_26 = "SP-R 26\""
    WARLORD = "16\" Warlord"
    FSS_PRO = "FSS 10.6\" Pro"
    FSS_NIGHTSHADE = "FSS Nightshade"
    HEAVY_BARREL = "25.9\" Heavy Barrel"
    XRK_LONGSHOT = "XRK LongShot Advantage"

    STRIKE_TEAM_159 = "15.9\" Strike Team", Game.COLD_WAR
    STRIKE_TEAM_183 = "18.3\" Strike Team", Game.COLD_WAR
    EXTENDED_BARREL_53 = "5.3\" Extended", Game.COLD_WAR
    TASK_FORCE_59 = "5.9\" Task Force", Game.COLD_WAR
    TASK_FORCE_72 = "7.2\" Task Force", Game.COLD_WAR
    TASK_FORCE_95 = "9.5\" Task Force", Game.COLD_WAR
    TASK_FORCE_103 = "10.3\" Task Force", Game.COLD_WAR
    TASK_FORCE_135 = "13.5\" Task Force", Game.COLD_WAR
    TASK_FORCE_195 = "19.5\" Task Force", Game.COLD_WAR
    TASK_FORCE_198 = "19.8\" Task Force", Game.COLD_WAR
    TASK_FORCE_205 = "20.5\" Task Force", Game.COLD_WAR
    TASK_FORCE_208 = "20.8\" Task Force", Game.COLD_WAR
    TASK_FORCE_218 = "21.8\" Task Force", Game.COLD_WAR
    CAVALRY_LANCER = "12.5\" Cavalry Lancer", Game.COLD_WAR
    RANGER_95 = "9.5\" Ranger", Game.COLD_WAR
    RANGER_197 = "19.7\" Ranger", Game.COLD_WAR
    RANGER_212 = "21.2\" Ranger", Game.COLD_WAR
    VDV_REINFORCED_93 = "9.3\" VDV Reinforced", Game.COLD_WAR
    VDV_REINFORCED_182 = "18.2\" VDV Reinforced", Game.COLD_WAR
    TAKEDOWN_137 = "13.7\" Takedown", Game.COLD_WAR
    TAKEDOWN_203 = "20.3\" Takedown", Game.COLD_WAR
    REINFORCED_HEAVY_61 = "6.1\" Reinforced Heavy", Game.COLD_WAR
    REINFORCED_HEAVY_195 = "19.5\" Reinforced Heavy", Game.COLD_WAR
    TIGER_TEAM_265 = "26.5\" Tiger Team", Game.COLD_WAR
    TITANIUM_163 = "16.3\" Titanium", Game.COLD_WAR
    TITANIUM_164 = "16.4\" Titanium", Game.COLD_WAR
    TITANIUM_17 = "17\" Titanium", Game.COLD_WAR
    LIBERATOR_81 = "8.1\" Liberator", Game.COLD_WAR
    LIBERATOR_20 = "20\" Liberator", Game.COLD_WAR
    RAPID_FIRE_17 = "17\" Rapid Fire", Game.COLD_WAR
    GRU_COMPOSITE = "16.2\" GRU Composite", Game.COLD_WAR


class Underbarrel(Attachment):
    COMMANDO_FOREGRIP = "Commando Foregrip"
    MERC_FOREGRIP = "Merc Foregrip"
    RANGER_FOREGRIP = "Ranger Foregrip"
    OPERATOR_FOREGRIP = "Operator Foregrip"
    STIPPLED_GRIP_TAPE = "Stippled Grip Tape"
    RUBBERIZED_GRIP_TAPE = "Rubberized Grip Tape"
    SNATCH_GRIP = "Snatch Grip"
    XRK_TRUEGRIP_TACTICAL = "XRK Truegrip Tactical"

    FIELD_AGENT_FOREGRIP = "Field Agent Foregrip", Game.COLD_WAR
    FIELD_AGENT_GRIP = "Field Agent Grip", Game.COLD_WAR
    FOREGRIP = "Foregrip", Game.COLD_WAR
    PATROL_FOREGIP = "Patrol Grip", Game.COLD_WAR
    SPETSNAZ_GRIP = "Spetsnaz Grip", Game.COLD_WAR
    SPETSNAZ_SPEEDGRIP = "Spetsnaz Speedgrip", Game.COLD_WAR
    BIPOD = "Bipod", Game.COLD_WAR
    SFOD_SPEEDGRIP = "SFOD Speedgrip", Game.COLD_WAR
    FRONT_GRIP = "Front Grip", Game.COLD_WAR
    SPETSNAZ_ERGONOMIC_GRIP = "Spetsnaz Ergonomic Grip", Game.COLD_WAR
    BRUISER_GRIP = "Bruiser Grip", Game.COLD_WAR
    INFILTRATOR_GRIP = "Infiltrator Grip", Game.COLD_WAR


class Optic(Attachment):
    VLK_3X_OPTIC = "VLK 3.0x Optic", Game.MODERN_WARFARE, ["vlk"]
    VARIABLE_ZOOM_SCOPE = "Variable Zoom Scope"
    SNIPER_SCOPE = "Sniper Scope"
    VIPER_REFLEX_SIGHT = "Viper Reflex Sight"
    OPERATOR_REFLEX_SIGHT = "Operator Reflex Sight"
    AIM_OP_REFLEX_SIGHT = "Aim-Op Reflex Sight"
    MONOCLE_REFLEX_SIGHT = "Monocle Reflex Sight"
    APX5_HOLOGRAPHIC_SIGHT = "APX5 Holographic Sight"
    GI_MINI_REFLEX = "G.I. Mini Reflex"
    CORP_COMBAT_HOLO_SIGHT = "Corp Combat Holo Sight"
    THERMAL_DUAL_POWER_SCOPE = "Thermal Dual Power Scope"
    MERC_THERMAL_OPTIC = "Merc Thermal Optic"
    THERMAL_HYBRID = "Thermal Hybrid"
    SCOUT_COMBAT_OPTIC = "Scout Combat Optic"
    THERMAL_SNIPER_SCOPE = "Thermal Sniper Scope"
    CANTED_HYBRID = "Canted Hybrid"
    INTEGRAL_HYBRID = "Integral Hybrid"
    CRONEN_MINI_REFLEX = "Cronen LP945 Mini Reflex"
    CRONEN_PRO = "Cronen C480 Pro Optic"
    FLIP_HYBRID = "4.0x Flip Hybrid"
    PBX_HOLO_SIGHT = "PBX Holo 7 Sight"
    SOLOZERO_ENHANCED = "Solozero NVG Enhanced"
    SOLOZERO_OPTICS_MINI_REFLEX = "Solozero Optics Mini Reflex"
    SOLOZERO_SPR = "Solozero SP-R 28mm"

    VISIONTECH = "Visiontech 2x", Game.COLD_WAR
    MILLSTOP_REFLEX = "Millstop Reflex", Game.COLD_WAR
    QUICKDOT_LED = "Quickdot LED", Game.COLD_WAR
    KOBRA_RED_DOT = "Kobra Red Dot", Game.COLD_WAR
    MICROFLEX_LED = "Microflex LED", Game.COLD_WAR
    AXIAL_ARMS = "Axial Arms 3x", Game.COLD_WAR
    SILLIX = "Sillix Holoscout", Game.COLD_WAR
    HAWKSMOOR = "Hawksmoor", Game.COLD_WAR
    VULTURE_CUSTOM = "Vulture Custom Zoom", Game.COLD_WAR


class Ammunition(Attachment):
    ROUND_MAGS_7 = "7 Round Mags"
    ROUND_MAGS_9 = "9 Round Mags"
    ROUND_MAGS_12 = "12 Round Mags"
    ROUND_MAGS_21 = "21 Round Mags"
    ROUND_MAGS_24 = "24 Round Mags"
    ROUND_DRUM_MAGS_25 = "25 Round Drum Mags"
    ROUND_MAGS_27 = "27 Round Mags"
    ROUND_MAGS_30 = "30 Round Mags"
    ROUND_MAGS_32 = "32 Round Mags"
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
    DRAGONS_BREATH_ROUNDS_8R = "8-R Dragon's Breath"
    HOLLOW_POINT = ".45 Hollow Point 12-R Mags"
    LAPAU_MAGS = ".338 Lapau Mag 5-R Mags"
    SPP_MAGS = "SPP 10-R Mags"
    NORMA_MAGS = ".300 Norma Mag 5-R Mags"
    ROUND_DRUMS_50 = "50 Round Drums"
    ROUND_DRUMS_100 = "100 Round Drums"
    CASKET_60 = "60 Round Casket Mags"

    RND_30 = "30 Rnd", Game.COLD_WAR
    RND_38 = "38 Rnd", Game.COLD_WAR
    RND_43 = "43 Rnd", Game.COLD_WAR
    RND_45 = "45 Rnd", Game.COLD_WAR
    RND_120 = "120 Rnd", Game.COLD_WAR
    RND_30_SPEED = "30 Rnd Speed Mag", Game.COLD_WAR
    RND_40_SPEED = "40 Rnd Speed Mag", Game.COLD_WAR
    RND_45_SPEED = "45 Rnd Speed Mag", Game.COLD_WAR
    STANAG_50 = "STANAG 50 Rnd Drum", Game.COLD_WAR
    STANAG_53 = "STANAG 53 Rnd Drum", Game.COLD_WAR
    STANAG_60 = "STANAG 60 Rnd Drum", Game.COLD_WAR
    SALVO_30 = "Salvo 30 Rnd Fast Mag", Game.COLD_WAR
    SALVO_50 = "Salvo 50 Rnd Fast Mag", Game.COLD_WAR
    SALVO_53 = "Salvo 53 Rnd Fast Mag", Game.COLD_WAR
    SALVO_54 = "Salvo 54 Rnd Fast Mag", Game.COLD_WAR
    SALVO_60 = "Salvo 60 Rnd Fast Mag", Game.COLD_WAR
    RND_DRUM_40 = "40 Rnd Drum", Game.COLD_WAR
    SPETSNAZ_DRUM_50 = "Spetsnaz 50 Rnd Drum", Game.COLD_WAR
    SPETSNAZ_60 = "Spetsnaz 60 Rnd", Game.COLD_WAR
    SPETSNAZ_150 = "Spetsnaz 150 Rnd", Game.COLD_WAR
    TAPED_MAGS = "Taped Mags", Game.COLD_WAR
    VDV_50 = "VDV 50 Rnd Fast Mag", Game.COLD_WAR
    FAST_MAG = "Fast Mag", Game.COLD_WAR


class RearGrip(Attachment):
    XRK_SPEED_GRIP = "XRK Speed Grip"
    XRK_VOID_II = "XRK Void II"
    STIPPLED_GRIP_TAPE = "Stippled Grip Tape"
    GRANULATED_GRIP_TAPE = "Granulated Grip Tape"
    RUBBERIZED_GRIP_TAPE = "Rubberized Grip Tape"
    CRONEN_SNIPER_ELITE = "Cronen Sniper Elite"
    CR_56_RUBBERIZED_WRAP = "CR-56 Rubberized Wrap"
    FTAC_G5_EXO = "FTAC G-5 EXO"

    SASR_JUNGLE = "SASR Jungle Grip", Game.COLD_WAR
    AIRBORNE_ELASTIC_WRAP = "Airborne Elastic Wrap", Game.COLD_WAR
    GRU_ELASTIC_WRAP = "GRU Elastic Wrap", Game.COLD_WAR
    SERPENT_WRAP = "Serpent Wrap", Game.COLD_WAR
    SPEED_TAPE = "Speed Tape", Game.COLD_WAR


class Stock(Attachment):
    NO_STOCK = "No Stock"
    FLY_STRAP = "Fly Strap"
    FSS_CLOSE_QUARTERS_STOCK = "FSS Close Quarters Stock"
    FTAC_COLLAPSIBLE = "FTAC Collapsible"
    FTAC_CHAMPION = "FTAC Champion"
    FTAC_SPORT_COMB = "FTAC Sport Comb"
    FTAC_STALKER_SCOUT = "FTAC Stalker Scout"
    SINGUARD_ARMS_EVADER = "Singuard Arms Evader"
    SINGUARD_ARMS_INVADER = "Singuard Arms Invader"
    SINGUARD_ARMS_ASSASSIN = "Singuard Arms Assassin"
    SINGUARD_ARMS_MARKSMAN = "Singuard Arms Marksman"
    SINGUARD_ARMS_SNIPER_PRO = "Singuard Arms Sniper Pro"
    FORGE_TAC_CQS = "FORGE TAC CQS"
    M13_SKELETON_STOCK = "M13 Skeleton Stock"
    FTAC_XL_ELITE_COMB = "FTAC XL Elite Comb"
    SKELETON_STOCK = "Skeleton Stock"
    FORGE_TAC_CQB_COMB = "FORGE TAC CQB Comb"
    FORGE_TAC_ULTRALIGHT = "FORGE TAC Ultralight"
    FSS_GUARDIAN = "FSS Guardian"
    STVOL_PRECISION_COMB = "STVOL Precision Comb"
    M16_STOCK = "M-16 Stock"
    XRK_SP_BLITZ = "XRK SP-LITE 208 Blitz"
    XRK_SP_ULTIMATE = "XRK SP-TAC 208 Ultimate"
    VLK_STRELOK = "VLK Strelok"
    VLK_VINTAZH = "VLK Vintazh"
    ISO_COLLAPSIBLE = "ISO Collapsible"

    WIRE_STOCK = "Wire Stock", Game.COLD_WAR
    RAIDER_PAD = "Raider Pad", Game.COLD_WAR
    RAIDER_STOCK = "Raider Stock", Game.COLD_WAR
    KGB_SKELETAL_STOCK = "KGB Skeletal Stock", Game.COLD_WAR
    SAS_COMBAT_STOCK = "SAS Combat Stock", Game.COLD_WAR
    TACTICAL_STOCK = "Tactical Stock", Game.COLD_WAR
    DUAL_WIELD = "Dual Wield", Game.COLD_WAR
    SPETSNAZ_PKM_STOCK = "Spetsnaz PKM Stock", Game.COLD_WAR
    CQB_PAD = "CQB Pad", Game.COLD_WAR


class Perk(Attachment):
    SLEIGHT_OF_HAND = "Sleight of Hand"
    PRESENCE_OF_MIND = "Presence of Mind"
    FMJ = "FMJ"
    FOCUS = "Focus"
    FULLY_LOADED = "Fully Loaded"
    AKIMBO = "Akimbo"
    FRANGIBLE_DISABLING = "Frangible Disabling"
    FRANGIBLE_WOUNDING = "Frangible - Wounding"


class Laser(Attachment):
    TAC_LASER = "Tac Laser"
    MW_LASER_1 = "1mW Laser"
    MW_LASER_5 = "5mW Laser"
    MW_LASER_5_SWAT = "SWAT 5mW Laser Sight", Game.COLD_WAR
    MW_LASER_5_GRU = "GRU 5mW Laser Sight", Game.COLD_WAR
    TIGER_TEAM_SPOTLIGHT = "Tiger Team Spotlight", Game.COLD_WAR
    STEADY_AIM_LASER = "Steady Aim Laser"


class TriggerAction(Attachment):
    LIGHTWEIGHT_TRIGGER = "Lightweight Trigger"


class Cable(Attachment):
    STRAND_CABLE_28 = "28-Strand Cable"


class Arms(Attachment):
    XRK_THUNDER_200 = "XRK Thunder 200 Lb"


class Bolt(Attachment):
    FTAC_FURY = "FTAC Fury 20\" Bolts"
