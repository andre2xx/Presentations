"""
S1.2-Ex2 : Convertir des tailles de fichiers
------------------------------------------------
Objectif :
Créer une fonction avec UN paramètre et PLUSIEURS returns qui convertit
une taille de fichier exprimée en bytes vers KB, MB et GB, puis
l'utiliser plusieurs fois.

Formules :
    1 KB = 1024 bytes
    1 MB = 1024 KB = 1024 x 1024 bytes
    1 GB = 1024 MB = 1024 x 1024 x 1024 bytes

Types utilisés :
    - int pour les calculs exacts (la taille en bytes)
    - float pour les résultats avec décimales (KB, MB, GB)

Données fournies :
    - Fichier 1 : 2048 bytes
    - Fichier 2 : 5242880 bytes (5 MB)
    - Fichier 3 : 1073741824 bytes (1 GB)
"""


def convertir_taille_fichier(taille_bytes):
    """
    Convertit une taille de fichier exprimée en bytes vers KB, MB et GB.

    Paramètre :
        taille_bytes (int) : la taille du fichier en bytes

    Retourne :
        tuple (float, float, float) : (taille en KB, taille en MB,
                                        taille en GB)
    """
    # TODO :
    # 1. Convertir bytes -> KB
    # 2. Convertir bytes -> MB
    # 3. Convertir bytes -> GB
    # 4. Retourner (ko, mo, go)
    pass


def main():
    # TODO :
    # 1. Appeler convertir_taille_fichier() pour 2048, 5242880 et
    #    1073741824 bytes
    # 2. Afficher chaque résultat avec 2 décimales (ex.: f"{valeur:.2f}")
    pass


if __name__ == "__main__":
    main()
