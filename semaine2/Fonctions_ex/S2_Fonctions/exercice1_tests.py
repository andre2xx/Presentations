
"""
Exercice 1 - Tests (pytest)
------------------------------------------------
IMPORTANT :
Ce fichier de tests importe votre programme complété. Pour que les tests
fonctionnent, enregistrez votre fichier complété sous le nom :

    exercice1.py

...dans le même dossier que ce fichier de tests, puis exécutez :

    pytest exercice1_tests.py

ou simplement :

    pytest

Seule la fonction construire_email() est testée automatiquement, car
afficher_profil() et main() dépendent de l'affichage/saisie clavier.
"""

from exercice1 import construire_email



def test_cas_1_minuscules():
    assert construire_email("jean", "dupont") == "jean.dupont@cegepoutaouais.qc.ca"


def test_cas_2_nom_majuscules():
    assert construire_email("paul", "DURAND") == "paul.DURAND@cegepoutaouais.qc.ca"


def test_cas_3_accent():
    assert construire_email("marie", "lévesque") == "marie.lévesque@cegepoutaouais.qc.ca"


def test_domaine_toujours_le_meme():
    email = construire_email("alice", "martin")
    assert email.endswith("@cegepoutaouais.qc.ca")


def test_format_general():
    assert construire_email("bob", "tremblay") == "bob.tremblay@cegepoutaouais.qc.ca"
