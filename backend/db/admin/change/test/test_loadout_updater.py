from db.admin.change.loadout_updater import _find_delimiter, find_weapon, _find_attachments
from model.weapon.new_attachment import Muzzle, Barrel, Optic, Underbarrel, Ammunition
from model.weapon.weapon import AssaultRifle

TEST_COMMAND = "!kilo"
TEST_RESPONSE = "@[user] Kilo: Monolithic Suppressor, Singuard 19.8, VLK/Holo (blue dot), Commando Foregrip, 60 Round Mags"


def test_find_weapon():
    assert AssaultRifle.KILO_141 == find_weapon(TEST_COMMAND)


def test_unable_to_find_weapon():
    assert find_weapon("!abc") is None


def test_find_attachments():
    expected = [
       Muzzle.MONOLITHIC_SUPPRESSOR,
       Barrel.SINGUARD_ARMS_198_PROWLER,
       Optic.VLK_30X_OPTIC,
       Underbarrel.COMMANDO_FOREGRIP,
       Ammunition.ROUND_MAGS_60
    ]
    actual = list(_find_attachments(AssaultRifle.KILO_141.attachments, TEST_RESPONSE).keys())
    assert expected == actual


def test_find_comma():
    assert "," == _find_delimiter(TEST_RESPONSE)


def test_find_hyphen():
    string = TEST_RESPONSE.replace(",", "-")
    assert "-" == _find_delimiter(string)
