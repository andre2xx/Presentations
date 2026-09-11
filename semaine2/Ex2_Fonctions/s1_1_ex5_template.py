"""
S1.1-Ex5 : Calculer le nombre d'hôtes disponibles dans un sous-réseau
------------------------------------------------
Objectif :
Créer une fonction avec paramètre et return qui calcule le nombre
d'hôtes disponibles dans un sous-réseau, à partir de sa notation CIDR
(le nombre après le "/"), puis l'utiliser plusieurs fois.

Formule :
    Nombre d'hôtes = 2 ** (32 - CIDR) - 2
    (on soustrait 2 pour l'adresse réseau et l'adresse broadcast)

    Opérateur puissance en Python : **
    Exemple : 2^8 s'écrit 2**8

Données fournies :
    - Sous-réseau 1 : /24
    - Sous-réseau 2 : /25
    - Sous-réseau 3 : /26
    - Sous-réseau 4 : /30
"""


def calculer_nombre_hotes(cidr):
    """
    Calcule le nombre d'hôtes disponibles dans un sous-réseau donné.

    Paramètre :
        cidr (int) : le nombre après le "/" dans la notation CIDR

    Retourne :
        int : le nombre d'hôtes disponibles (adresse réseau et
              broadcast exclues)
    """
    # TODO : à compléter
    sous_reseau= 2 ** (32 - cidr) - 2
    return int(sous_reseau)




def main():
    # TODO :
    # 1. Appeler calculer_nombre_hotes() pour /24, /25, /26 et /30
    sous_reseau_1 = calculer_nombre_hotes(24)
    sous_reseau_2 = calculer_nombre_hotes(25)
    sous_reseau_3 = calculer_nombre_hotes(26)
    sous_reseau_4 = calculer_nombre_hotes(30)

    # 2. Afficher les résultats
    print("Le nombre d'hotes disponible pour un réseau de /24 est : ", sous_reseau_1)
    print("Le nombre d'hotes disponible pour un réseau de /25 est : ", sous_reseau_2)
    print("Le nombre d'hotes disponible pour un réseau de /26 est : ", sous_reseau_3)
    print("Le nombre d'hotes disponible pour un réseau de /30 est : ", sous_reseau_4)

if __name__ == "__main__":
    main()
