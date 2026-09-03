"""
S1.1-Ex2 : Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "s1_1_ex2.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest s1_1_ex2_tests.py
"""

import pytest

from s1_1_ex2_template import mbps_vers_mo_par_seconde


def test_100_mbps():
    assert mbps_vers_mo_par_seconde(100) == 12.5


def test_500_mbps():
    assert mbps_vers_mo_par_seconde(500) == 62.5


def test_1000_mbps():
    assert mbps_vers_mo_par_seconde(1000) == 125.0


def test_zero():
    assert mbps_vers_mo_par_seconde(0) == 0


def test_valeur_non_entiere():
    assert mbps_vers_mo_par_seconde(8) == pytest.approx(1.0)
