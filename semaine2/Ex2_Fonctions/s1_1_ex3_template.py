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


def calculer_temps_telechargement(taille_gb: float, vitesse_mbps: float) -> tuple:
    """
    Calcule le temps de téléchargement d'un fichier.

    Paramètres :
        taille_gb (float)   : la taille du fichier en GB
        vitesse_mbps (float) : la vitesse de connexion en Mbps

    Retourne :
        tuple (float, float) : (temps en secondes, temps en minutes)
    """
    # 1. Convertir la taille du fichier en MB
    taille_mb = taille_gb * 1024
    # 2. Convertir la vitesse en MB/s
    vitesse_mbs = vitesse_mbps / 8
    # 3. Calculer le temps en secondes
    temps_seconde = taille_mb / vitesse_mbs
    # 4. Convertir le temps en minutes
    temps_min = temps_seconde / 60
    # 5. Retourner (temps_secondes, temps_minutes)
    return temps_seconde, temps_min



def main():
    #
    # 1. Appeler calculer_temps_telechargement() avec 4.7 GB et 50 Mbps
    seconde, minutes = calculer_temps_telechargement(4.7, 50)
    # 2. Afficher le temps en secondes et en minutes
    print(f"temps de télécharhgement en seconde :  {minutes:.1f}\ntemps de téléchargement en temps minutes : {minutes:.2f}")



if __name__ == "__main__":
    main()
