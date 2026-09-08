"""
Demander nb_maisons
nb_bonbons_total = 0
répéter pour nb_maisons
    Demander nb_bonbons_maisons
    nb_bonbons_total = nb_bonbons_total +nb_bonbon_maisons
affciher nb_bonbons_total
"""


nb_maisons = int(input("Combien de maisons va-tu visiter ?"))
nb_bonbons_total = 0
for i in range(nb_maisons):
    nb_bonbons_maisons = int(input("Combien de bonbons tu as reçu ?"))
    nb_bonbons_total = nb_bonbons_total + nb_bonbons_maisons
print("Nomnbre de bonbons total : ", nb_bonbons_total)
