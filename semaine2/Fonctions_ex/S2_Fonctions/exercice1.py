"""
Exercice 1 - Création d'un profil utilisateur
------------------------------------------------
Objectif :
Écrire un programme qui récupère les informations d'un utilisateur
(nom, prénom, date de naissance, profession, adresse de résidence)
et qui construit automatiquement une adresse courriel selon le format :

    [prenom].[nom]@cegepoutaouais.qc.ca

Le profil complet doit ensuite être affiché à l'écran de façon
professionnelle (utilisez f-strings et une mise en forme soignée).

NOTE IMPORTANTE :
L'adresse courriel doit respecter EXACTEMENT la casse (majuscules/minuscules)
telle que saisie par l'utilisateur. Ne transformez donc pas les lettres.
Ex.: nom="DURAND", prenom="paul" -> "paul.DURAND@cegepoutaouais.qc.ca"
"""

DOMAINE = "cegepoutaouais.qc.ca"


def construire_email(prenom, nom):
    """
    Construit et retourne l'adresse courriel d'un utilisateur selon le
    format : prenom.nom@cegepoutaouais.qc.ca

    Paramètres :
        prenom (str) : le prénom de l'utilisateur
        nom (str)    : le nom de l'utilisateur

    Retourne :
        str : l'adresse courriel construite
    """
    # TODO : construire et retourner l'adresse courriel
    courriel = f"{prenom}.{nom}@{DOMAINE}"
    return courriel


def afficher_profil(nom, prenom, date_naissance, profession, adresse):
    """
    Affiche à l'écran le profil complet de l'utilisateur de façon
    professionnelle, incluant l'adresse courriel générée automatiquement.

    Paramètres :
        nom (str)
        prenom (str)
        date_naissance (str)
        profession (str)
        adresse (str)
    """
    # TODO :
    # 1. Construire l'adresse courriel à l'aide de construire_email()
    courriel = construire_email(prenom, nom)

    # 2. Afficher un profil bien formaté (titre, séparateurs, etc.)
    print("******************************************")
    print("*****************profil*******************")
    print(f"*   nom : {nom}                         *")
    print(f"*   prenom : {prenom}                   *")
    print(f"*   date de naissance : {date_naissance}*")
    print(f"    profession : {profession}           *")
    print(f"*   courriel : {courriel}               *")
    print(f"*   adresse : {adresse}                 *")



def main():
    """
    Récupère les informations de l'utilisateur au clavier (input) puis
    affiche son profil complet.
    """
    # TODO :
    # 1. Demander à l'utilisateur : nom, prénom, date de naissance,
    #    profession, adresse de résidence
    nom = input("Entrer votre nom: ")
    prenom = input("entrer votre prenom: ")
    date_naissance = input("Entrer votre date de naissance: ")
    profession = input("entrer votre profession: ")
    adresse = input("entrer votre adreesse: ")

    # 2. Appeler afficher_profil() avec ces informations
    afficher_profil(nom, prenom, date_naissance, profession, adresse)



if __name__ == "__main__":
    main()
