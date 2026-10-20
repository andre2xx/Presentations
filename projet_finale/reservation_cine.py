#######################################################################################
#Entrées : nom_client, age_client, nom_film, nombre_billet, heure_film, siege_choisi, reserver_billet
#sorties : confirmer_reservation, heure_film, numero_salle, prix_totale, billet_achete,
#menu_principale, liste_films, numero_salle, plan_salle
#######################################################################################
#AFFICHER menu_principale():
# 1- liste film
# 2- reserver billet
# 3- horaire des films
# 4- les tarifs
# 5- quitter
#SI choix == 1:
#   afficher liste_film()
#SI choix == 2:
#    creer_reservation()
#SI choix == 3
#   afficher l'horaires des films
#SI choix == 4:
#   afficher les tarifs
#SI choix == 5:
#   Quitter.
#############################################################################################
#creer reservation():
#DEMANDER nom_client, nom_film, nombre_billet
#POUR CHAQUE billet dans nombre_billet:
#   DEMANDER age_client
#       SI 3 < age <= 13:
#           tarif = enfants(12$)
#       SI age >= 14:
#           tarif = adulte(15$)
#       Si age == "etudiant":
#           tarif = etudiant(12)"
#############################################################################################
#choisir_siege():
#Afficher liste_siege
#DEMANDER choisir un siege dans liste_siege
#
