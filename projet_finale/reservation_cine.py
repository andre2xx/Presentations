#######################################################################################
#Entrées : nom_client, age_client, nom_film, nombre_billet, heure_film, siege_choisi, option_vip, vip_nourriture
#sorties : confirmation_reservation, heure_film, numero_salle, prix_totale, billet_achete,facture,
#menu_principale, liste_films, liste_siege
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
#    reserver billet()
#SI choix == 3
#   afficher l'horaires des films
#SI choix == 4:
#   afficher tarifs():
#############################################################################################
#afficher_filmS():
#AFFICHER liste_film
#"0" pour retourner au menu principale
#############################################################################################
#reserver_billets():
#DEMANDER nom_client
#DEMANDER nom_film
#DEMANDER nombre_billet
#
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
#While True
#   Afficher liste_siege
#   DEMANDER choisir un siege dans liste_siege
#   AJOUTER selection à siege_chosi
#   DEMANDER ajouter d'autre billet?
#       SI reponse == "non"
#           break
#       Sinon si reponse == "oui"
#           continue
#retourner siege_chosi
###############################################################################################
