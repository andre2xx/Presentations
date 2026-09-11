"""
S1.1-Ex5 : Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "s1_1_ex5.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest s1_1_ex5_tests.py
"""

from s1_1_ex5_template import calculer_nombre_hotes


def test_slash_24():
    assert calculer_nombre_hotes(24) == 254


def test_slash_25():
    assert calculer_nombre_hotes(25) == 126


def test_slash_26():
    assert calculer_nombre_hotes(26) == 62


def test_slash_30():
    assert calculer_nombre_hotes(30) == 2


def test_slash_16():
    assert calculer_nombre_hotes(16) == 65534


def test_retourne_un_entier():
    assert isinstance(calculer_nombre_hotes(24), int)
