import json
from db.loadout_updater import _find_delimiter, find_weapon, _find_attachments, _compare_weapon_counterpart, _split_on_token, _find_loadout, DUAL_GAME_WEAPONS
from model.game import Game
from model.weapon.attachment import Muzzle, Barrel, Optic, Underbarrel, Ammunition
from model.weapon.weapon import AssaultRifle, SubmachineGun, TacticalRifle

KILO_RESPONSE = "@[user] Kilo: Monolithic Suppressor, Singuard 19.8, VLK/Holo (blue dot), Commando Foregrip, 60 Round Mags"
AUG_RESPONSE = "Arial 3x, Strike Team Barrel, Agency Suppressor, Field Agent Grip, 45 Rnd Mag"
LEGACY_DATABASE = "db/test/legacy-database.json"


def test_find_weapon():
    assert AssaultRifle.KILO_141 == find_weapon("!kilo")


def test_unable_to_find_weapon():
    assert find_weapon("!abc") is None


def test_find_attachments():
    expected = [
        Ammunition.ROUND_MAGS_60,
        Underbarrel.COMMANDO_FOREGRIP,
        Optic.CORP_COMBAT_HOLO_SIGHT,
        Barrel.SINGUARD_ARMS_198_PROWLER,
        Muzzle.MONOLITHIC_SUPPRESSOR,
    ]
    actual = list(_find_attachments(AssaultRifle.KILO_141, KILO_RESPONSE).keys())
    assert expected == actual


def test_cw_weapon_selected():
    weak_attachments = {i: 10 for i in range(5)}
    weapon, _ = _compare_weapon_counterpart(SubmachineGun.AUG, weak_attachments, AUG_RESPONSE)
    assert TacticalRifle.AUG_CW == weapon


def test_mw_weapon_selected():
    strong_attachments = {i: 100 for i in range(5)}
    weapon, _ = _compare_weapon_counterpart(SubmachineGun.AUG, strong_attachments, AUG_RESPONSE)
    assert SubmachineGun.AUG == weapon


def test_find_comma():
    assert "," == _find_delimiter(KILO_RESPONSE)


def test_find_hyphen():
    response = KILO_RESPONSE.replace(",", "-")
    assert "-" == _find_delimiter(response)


def test_split_on_and():
    token = " and "
    joined_attachments = ["60 Round Mags and Stippled Grip Tape"]
    separated_attachments = ["60 Round Mags", "Stippled Grip Tape"]

    assert separated_attachments == _split_on_token(joined_attachments, token)
    assert separated_attachments == _split_on_token(separated_attachments, token)


def test_against_legacy_database():
    total = success = 0

    with open(LEGACY_DATABASE, "r+") as file:
        players = json.load(file)

    for name, player in players.items():
        for command, response in player["commands"].items():

            loadout = _find_loadout(command, response)

            if loadout is None:
                continue

            weapon, attachments = loadout
            weapon_name = str(weapon)

            if weapon.game == Game.COLD_WAR and weapon in DUAL_GAME_WEAPONS:
                weapon_name += " CW"

            old_loadout = player["loadouts"].get(weapon_name)

            if old_loadout is None:
                continue

            old_attachments = [_sanitise_legacy_attachment(a) for a in old_loadout["attachments"].values()]
            new_attachments = [str(a).lower() for a in attachments.keys()]

            if sorted(old_attachments) == sorted(new_attachments):
                success += 1

            total += 1

    assert 91 == total == success


def _sanitise_legacy_attachment(a: str) -> str:
    return a \
        .lower() \
        .replace("\"", "") \
        .replace("20.3 takedown", "takedown") \
        .replace("5.9 task force", "task force") \
        .replace("19.5 task force", "task force") \
        .replace("20.3 task force", "task force") \
        .replace("16.3 titanium", "titanium") \
        .replace("17 titanium", "titanium") \
        .replace("20 liberator", "liberator") \
        .replace("21.2 ranger", "ranger") \
        .replace("32.0 factory barrel", "32 factory barrel") \
        .replace("19.5 reinforced heavy", "reinforced heavy") \
        .replace("collosus suppressor", "colossus suppressor") \
        .replace("ftac stalker scout", "ftac stalker-scout") \
        .replace("muzzle brake 5.56", "muzzle brake") \
        .replace("stanag 50 rnd drum", "stanag 50 rnd")

