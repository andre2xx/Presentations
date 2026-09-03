"""
S1.1-Ex3 : Calculer le temps de téléchargement d'un fichier
------------------------------------------------
Objectif :
Créer une fonction avec plusieurs paramètres et plusieurs returns qui
calcule le temps de téléchargement d'un fichier, à partir de sa taille
(en GB) et de la vitesse de connexion (en Mbps).

Formules :
    Taille en MB   = Taille en GB x 1024
    Vitesse en MB/s = Vitesse en Mbps / 8
    Temps (secondes) = Taille (MB) / Vitesse (MB/s)
    Temps (minutes)  = Temps (secondes) / 60

Données fournies :
    - Taille du fichier      : 4.7 GB (image ISO)
    - Vitesse de téléchargement : 50 Mbps
"""


def calculer_temps_telechargement(taille_gb, vitesse_mbps):
    """
    Calcule le temps de téléchargement d'un fichier.

    Paramètres :
        taille_gb (float)   : la taille du fichier en GB
        vitesse_mbps (float) : la vitesse de connexion en Mbps

    Retourne :
        tuple (float, float) : (temps en secondes, temps en minutes)
    """
    # TODO :
    # 1. Convertir la taille du fichier en MB
    # 2. Convertir la vitesse en MB/s
    # 3. Calculer le temps en secondes
    # 4. Convertir le temps en minutes
    # 5. Retourner (temps_secondes, temps_minutes)
    pass


def main():
    # TODO :
    # 1. Appeler calculer_temps_telechargement() avec 4.7 GB et 50 Mbps
    # 2. Afficher le temps en secondes et en minutes
    pass


if __name__ == "__main__":
    main()
