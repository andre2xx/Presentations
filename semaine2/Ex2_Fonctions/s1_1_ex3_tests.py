"""
S1.1-Ex3 : Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "s1_1_ex3.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest s1_1_ex3_tests.py
"""

import pytest

from s1_1_ex3_template import calculer_temps_telechargement


def test_retourne_un_tuple_de_deux_valeurs():
    resultat = calculer_temps_telechargement(4.7, 50)
    assert isinstance(resultat, tuple)
    assert len(resultat) == 2


def test_cas_enonce_4_7gb_50mbps():
    secondes, minutes = calculer_temps_telechargement(4.7, 50)
    assert secondes == pytest.approx(770.048, abs=0.01)
    assert minutes == pytest.approx(12.8341, abs=0.01)


def test_relation_minutes_secondes():
    secondes, minutes = calculer_temps_telechargement(1, 100)
    assert minutes == pytest.approx(secondes / 60)


def test_taille_1gb_vitesse_8mbps():
    # 1 GB = 1024 MB ; 8 Mbps = 1 MB/s -> 1024 secondes
    secondes, minutes = calculer_temps_telechargement(1, 8)
    assert secondes == pytest.approx(1024.0, abs=0.01)
    assert minutes == pytest.approx(1024.0 / 60, abs=0.01)


def test_petite_valeur():
    secondes, minutes = calculer_temps_telechargement(0, 50)
    assert secondes == 0
    assert minutes == 0
