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


def calculer_debit(vitesse_mbps: float)-> float:
    """
    Calcule le débit théorique en MB/s à partir d'une vitesse en Mbps.

    Paramètre :
        vitesse_mbps (float) : la vitesse de connexion en Mbps

    Retourne :
        float : le débit théorique en MB/s
    """
    #
    debit_mbs = vitesse_mbps / 8
    return debit_mbs


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
    temps_telechargement_sec = taille_mb / debit_mo_par_seconde
    temps_telechargement_min = temps_telechargement_sec / 60
    return temps_telechargement_sec, temps_telechargement_min



def main():
    # TODO :
    # 1. Calculer le débit avec calculer_debit() pour 100 Mbps
    debit = calculer_debit(100)
    # 2. Pour chaque taille de fichier (100 MB, 1 GB = 1024 MB,
    #    5 GB = 5120 MB), calculer et afficher le temps de
    #    téléchargement en secondes et en minutes
    seconde_100, minutes_100 = calculer_temps_telechargement(100, debit)
    print(f"100 mb -> {seconde_100:.2f} sec ({minutes_100:.2f} min)")
    seconde_1go, minutes_1go = calculer_temps_telechargement(1024, debit)
    print(f"1 GB -> {seconde_1go:.2f} sec ({minutes_1go:.2f} min)")
    seconde_5go, minutes_5go = calculer_temps_telechargement(5120, debit)
    print(f"5 GB mb -> {seconde_5go:.2f} sec ({minutes_5go:.2f} min)")



if __name__ == "__main__":
    main()
