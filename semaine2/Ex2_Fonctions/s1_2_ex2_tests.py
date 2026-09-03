"""
S1.2-Ex2 : Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "s1_2_ex2.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest s1_2_ex2_tests.py
"""

import pytest

from s1_2_ex2 import convertir_taille_fichier


def test_retourne_un_tuple_de_trois_valeurs():
    resultat = convertir_taille_fichier(2048)
    assert isinstance(resultat, tuple)
    assert len(resultat) == 3


def test_2048_bytes():
    ko, mo, go = convertir_taille_fichier(2048)
    assert ko == pytest.approx(2.0)
    assert mo == pytest.approx(2048 / (1024 ** 2))
    assert go == pytest.approx(2048 / (1024 ** 3))


def test_5mb_fichier():
    ko, mo, go = convertir_taille_fichier(5242880)
    assert mo == pytest.approx(5.0)


def test_1gb_fichier():
    ko, mo, go = convertir_taille_fichier(1073741824)
    assert go == pytest.approx(1.0)


def test_zero_bytes():
    ko, mo, go = convertir_taille_fichier(0)
    assert (ko, mo, go) == (0, 0, 0)
