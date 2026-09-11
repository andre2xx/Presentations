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
    ko = taille_bytes / 1024
    # 2. Convertir bytes -> MB
    mo = taille_bytes / (1024 * 1024)
    # 3. Convertir bytes -> GB
    go = taille_bytes / (1024 * 1024 *1024)
    # 4. Retourner (ko, mo, go)
    return ko, mo, go


def main():
    # TODO :
    # 1. Appeler convertir_taille_fichier() pour 2048, 5242880 et
    #    1073741824 bytes
    ko, mo, go = convertir_taille_fichier(2048)
    ko2, mo2, go2 = convertir_taille_fichier(5242880)
    ko3, mo3, go3 = convertir_taille_fichier(1073741824)
    # 2. Afficher chaque résultat avec 2 décimales (ex.: f"{valeur:.2f}")
    print(f"{2048} bytes en ko, mo et go : {ko:.2f} kb = {mo:.2f} mo = {go:.2f} go")
    print(f"{5242880} bytes en ko, mo et go : {ko2:.2f} kb = {mo2:.2f} mo = {go2:.2f} go")
    print(f"{1073741824} bytes en ko, mo et go : {ko3:.2f} kb = {mo3:.2f} mo = {go3:.2f} go")




if __name__ == "__main__":
    main()
