"""
S1.1-Ex2 : Convertir des vitesses de transfert (Mbps -> MB/s)
------------------------------------------------
Objectif :
Créer une fonction avec paramètre et return qui convertit une vitesse
donnée en Mbps (mégabits par seconde) vers des MB/s (mégaoctets par
seconde), puis l'utiliser plusieurs fois.

Formule :
    MB/s = Mbps / 8       (1 octet = 8 bits)

Données fournies :
    - Vitesse de connexion 1 : 100 Mbps
    - Vitesse de connexion 2 : 500 Mbps
    - Vitesse de connexion 3 : 1000 Mbps (1 Gbps)
"""


def mbps_vers_mo_par_seconde(vitesse_mbps):
    """
    Convertit une vitesse exprimée en Mbps vers des MB/s.

    Paramètre :
        vitesse_mbps (float) : la vitesse en mégabits par seconde

    Retourne :
        float : la vitesse équivalente en mégaoctets par seconde (MB/s)
    """
    # TODO : à compléter
    pass


def main():
    # TODO :
    # 1. Appeler mbps_vers_mo_par_seconde() pour 100, 500 et 1000 Mbps
    # 2. Afficher les 3 résultats de façon claire
    vitesse1_mbps = 100
    vitesse2_mbps = 500
    vitesse3_mbps = 1000
    vitesse1_mbs = mbps_vers_mo_par_seconde(vitesse1_mbps)
    vitesse2_mbs = mbps_vers_mo_par_seconde(vitesse2_mbps)
    vitesse3_mbs = mbps_vers_mo_par_seconde(vitesse3_mbps)
    print(f"{vitesse3_mbps}")


if __name__ == "__main__":
    main()
