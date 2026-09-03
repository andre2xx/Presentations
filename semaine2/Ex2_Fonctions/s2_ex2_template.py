"""
S2-Ex2 : Calculer le débit théorique et le temps de téléchargement
------------------------------------------------
Objectif :
Créer DEUX fonctions :
    1. Une pour calculer le débit théorique (en MB/s) à partir d'une
       vitesse de connexion en Mbps.
    2. Une pour calculer le temps de téléchargement (en secondes et en
       minutes) à partir d'une taille de fichier (en MB) et du débit
       calculé (en MB/s).

Contexte :
Un technicien teste une nouvelle connexion Internet. Il veut connaître
le débit théorique maximum et le temps de téléchargement pour
différentes tailles de fichiers.

Formules :
    1 GB = 1024 MB
    Débit en MB/s = Vitesse en Mbps / 8
    Temps de téléchargement (sec) = Taille fichier (MB) / Débit (MB/s)
    Temps en minutes = Temps en secondes / 60

Données fournies :
    - Vitesse de connexion : 100 Mbps (vous pouvez utiliser une autre
      valeur pour vos tests, mais gardez celle-ci pour l'affichage final)
    - Fichiers à télécharger : 100 MB, 1 GB et 5 GB
"""


def calculer_debit(vitesse_mbps):
    """
    Calcule le débit théorique en MB/s à partir d'une vitesse en Mbps.

    Paramètre :
        vitesse_mbps (float) : la vitesse de connexion en Mbps

    Retourne :
        float : le débit théorique en MB/s
    """
    # TODO : à compléter
    pass


def calculer_temps_telechargement(taille_mb, debit_mo_par_seconde):
    """
    Calcule le temps de téléchargement d'un fichier.

    Paramètres :
        taille_mb (float)            : la taille du fichier en MB
        debit_mo_par_seconde (float) : le débit de la connexion en MB/s

    Retourne :
        tuple (float, float) : (temps en secondes, temps en minutes)
    """
    # TODO : à compléter
    pass


def main():
    # TODO :
    # 1. Calculer le débit avec calculer_debit() pour 100 Mbps
    # 2. Pour chaque taille de fichier (100 MB, 1 GB = 1024 MB,
    #    5 GB = 5120 MB), calculer et afficher le temps de
    #    téléchargement en secondes et en minutes
    pass


if __name__ == "__main__":
    main()
