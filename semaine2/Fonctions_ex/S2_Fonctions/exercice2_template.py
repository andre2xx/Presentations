"""
Exercice 2 - Vérification de plage de valeurs
------------------------------------------------
Objectif :
Écrire un programme qui vérifie automatiquement si une valeur
(ex. : prix d'une action, taux d'intérêt) se situe dans une plage
définie par un seuil inférieur et un seuil supérieur (bornes incluses).

Le programme doit indiquer clairement si la valeur respecte ou non
la plage donnée.
"""


def verifier_plage(valeur, seuil_inferieur, seuil_superieur):
    """
    Vérifie si 'valeur' se situe entre 'seuil_inferieur' et
    'seuil_superieur' (bornes incluses).

    Paramètres :
        valeur (float)          : la valeur à vérifier
        seuil_inferieur (float) : la borne inférieure de la plage
        seuil_superieur (float) : la borne supérieure de la plage

    Retourne :
        bool : True si la valeur est dans la plage (bornes incluses),
               False sinon
    """
    # TODO : à compléter
    pass


def afficher_resultat(valeur, seuil_inferieur, seuil_superieur):
    """
    Affiche à l'écran si la valeur donnée respecte ou non la plage,
    de façon claire et professionnelle.
    """
    # TODO :
    # 1. Appeler verifier_plage()
    # 2. Afficher un message clair selon le résultat
    pass


def main():
    """
    Récupère au clavier la valeur à vérifier ainsi que les seuils,
    puis affiche le résultat.
    """
    # TODO :
    # 1. Demander à l'utilisateur : la valeur, le seuil inférieur,
    #    le seuil supérieur (convertir en float)
    # 2. Appeler afficher_resultat() avec ces informations
    pass


if __name__ == "__main__":
    main()
