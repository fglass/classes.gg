from db.loadout_updater import _find_delimiter, find_weapon, _find_attachments, _compare_weapon_counterpart
from model.weapon.attachment import Muzzle, Barrel, Optic, Underbarrel, Ammunition
from model.weapon.weapon import AssaultRifle, SubmachineGun, TacticalRifle

KILO_RESPONSE = "@[user] Kilo: Monolithic Suppressor, Singuard 19.8, VLK/Holo (blue dot), Commando Foregrip, 60 Round Mags"
AUG_RESPONSE = "Arial 3x, Strike Team Barrel, Agency Suppressor, Field Agent Grip, 45 Rnd Mag"


def test_find_weapon():
    assert AssaultRifle.KILO_141 == find_weapon("!kilo")


def test_unable_to_find_weapon():
    assert find_weapon("!abc") is None


def test_find_attachments():
    expected = [
        Ammunition.ROUND_MAGS_60,
        Underbarrel.COMMANDO_FOREGRIP,
        Optic.VLK_30X_OPTIC,
        Barrel.SINGUARD_ARMS_198_PROWLER,
        Muzzle.MONOLITHIC_SUPPRESSOR,
    ]
    actual = list(_find_attachments(AssaultRifle.KILO_141.attachments, KILO_RESPONSE).keys())
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
