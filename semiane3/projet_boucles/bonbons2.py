"""
Demander objectif_bonbons
nb_bonbons_total = 0
REPETER TANT QUE nb_bonbons_total < objectif_bonbons
    DEMANDER nb_bonbons_maisons
    nb_bonbons_total = nb_bonbons_total + nb_bonbons_maison
Afficher nb_bonbons_total
"""


objectif_bonbons = int(input("Combien de bonbons souhaites-tu rammaser ?: "))
nb_bonbons_total = 0
while nb_bonbons_total < objectif_bonbons:
    nb_bonbons_maisons = int(input("Combien de bonbons as tu recu ? :"))
    nb_bonbons_total = nb_bonbons_total + nb_bonbons_maisons
print("Nombre de bonbons total : ", nb_bonbons_total)