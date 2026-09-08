"""
Exercice 2 - Tests (pytest)
------------------------------------------------
IMPORTANT :
Enregistrez votre fichier complété sous le nom "exercice2.py" dans le
même dossier que ce fichier de tests, puis exécutez :

    pytest exercice2_tests.py

Résultats attendus (calculés à partir du plan de tests de l'énoncé) :

    Valeur   Seuil inf.  Seuil sup.  Résultat attendu
    134.73   120         139         True
    10.5     9.8         10.5        True   (borne supérieure incluse)
    228.67   137.62      228.65      False  (dépasse la borne sup.)
    74.22    71.13       77.16       True
    57.30    57.30       68.74       True   (borne inférieure incluse)
"""
from exercice2 import verifier_plage


def test_cas_1_dans_la_plage():
    assert verifier_plage(134.73, 120, 139) is True


def test_cas_2_egal_borne_superieure():
    assert verifier_plage(10.5, 9.8, 10.5) is True


def test_cas_3_hors_plage():
    assert verifier_plage(228.67, 137.62, 228.65) is False


def test_cas_4_dans_la_plage():
    assert verifier_plage(74.22, 71.13, 77.16) is True


def test_cas_5_egal_borne_inferieure():
    assert verifier_plage(57.30, 57.30, 68.74) is True


def test_valeur_juste_sous_la_borne_inf():
    assert verifier_plage(56.99, 57.30, 68.74) is False


def test_valeur_juste_au_dessus_de_la_borne_sup():
    assert verifier_plage(228.66, 137.62, 228.65) is False
