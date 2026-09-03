"""
S2-Ex2 : Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "s2_ex2.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest s2_ex2_tests.py
"""

import pytest

from s2_ex2 import calculer_debit, calculer_temps_telechargement


def test_debit_100_mbps():
    assert calculer_debit(100) == 12.5


def test_debit_8_mbps():
    assert calculer_debit(8) == 1.0


def test_debit_0_mbps():
    assert calculer_debit(0) == 0


def test_retourne_un_tuple_de_deux_valeurs():
    resultat = calculer_temps_telechargement(100, 12.5)
    assert isinstance(resultat, tuple)
    assert len(resultat) == 2


def test_fichier_100mb_debit_12_5():
    secondes, minutes = calculer_temps_telechargement(100, 12.5)
    assert secondes == pytest.approx(8.0)
    assert minutes == pytest.approx(8.0 / 60)


def test_fichier_1gb_debit_12_5():
    secondes, minutes = calculer_temps_telechargement(1024, 12.5)
    assert secondes == pytest.approx(81.92, abs=0.01)
    assert minutes == pytest.approx(81.92 / 60, abs=0.01)


def test_fichier_5gb_debit_12_5():
    secondes, minutes = calculer_temps_telechargement(5120, 12.5)
    assert secondes == pytest.approx(409.6, abs=0.01)
    assert minutes == pytest.approx(409.6 / 60, abs=0.01)


def test_integration_avec_calculer_debit():
    debit = calculer_debit(100)
    secondes, minutes = calculer_temps_telechargement(100, debit)
    assert secondes == pytest.approx(8.0)
