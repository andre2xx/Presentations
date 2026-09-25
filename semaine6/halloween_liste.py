"""
Entrées: nb_maisons (int), nb_bonbons_maison(int) -> ls_bonbon (list)
Sorties:nb_bonbons_total(int), nb_maison_donne_bonbons(int)
pseudocode:
DEMANDER nb_amisons                                 3
INITIALISER ls_maison                               []
Pour nb_maisons                                     for 3
    DEMANDER nb_bonbons_maison                          5   0   6
    METTRE nb_bonbons_maison Dans ls_bobon              [5, 0, 6]
nb_bonbons_total = SOMME de ls_bonbon               11
nb_zero = 0
POUR nb_bonbon DANS ls_bonbon
    SI nb_bonbon == 0
        nb_zero = nb_zero + 1
nb_maison_donne_bonbons = LONGEUR DE ls_bonbon = nb_zero                           2
AFFICHER nb_bonbon_total, nb_maison_donne_bonbon

"""
nb_maisons = int(input("Combien de bonbon tu veuyx visitter ? : "))
ls_bonbon =[]
for i in range(nb_maisons):
    nb_bonbons_maison = int(input("Combien de bonbon tu as reçu ? : "))
    ls_bonbon.append(nb_bonbons_maison)
nb_bonbons_total = sum(ls_bonbon)
nb_zero = 0
for nb_bonbon in ls_bonbon:
    if nb_bonbon == 0:
        nb_zero = nb_zero + 1
nb_maison_donne_bonbons = len(ls_bonbon) - nb_zero
print("Nombre de bonbon totale: ", nb_bonbons_total)
print("Nombre de maison qui donnent des bonbons :", nb_maison_donne_bonbons)