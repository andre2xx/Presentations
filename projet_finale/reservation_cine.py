#######################################################################################
#Entrées : nom_client, type_billet, nb_billet, heure_film, siege_choisi, vip_nourriture
#sorties : confirmation_reservation, heure_film, numero_salle, prix_totale, billet_achete,facture,
#menu_principale, liste_films, liste_siege
################################################################################################
#valeurs constante: liste_film, horaire_films, tarifs, taux_taxes = 1.14975
###############################################################################################
#FONCTIONS: menu_principale(), afficher_film(), reserver_billets, modifier_resevration, creer_facture,
# afficher_horaire, afficher_tarifs, creer_confirmation, choisir_siege,
################################################################################################
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
#SI choix == 5:
#   AFFICHER "Merci et à bientôt !"
#   ARRETER le programme
#SINON:
#   AFFICHER "Choix invalide"
#   REAFFICHER le menu
#############################################################################################
#afficher_filmS():
#AFFICHER liste_film
#"0" pour retourner au menu principale
#############################################################################################
#reserver_billets():
#DEMANDER nom_client
#DEMANDER nom_film
#DEMANDER heure_film
#DEAMNDER type_billet
#DEMANDER nombre_billet

#SI nom_client == vide:
#   AFFICHER "Le nom ne peut pas être vide"
#   REDemander le nom

#SI nom_client contient des chiffres:
#   AFFICHER "Le nom ne doit pas contenir de chiffres"
#   REDemander le nom

#VERIFIER si des places sont disponibles
#SI aucune place n'est disponible:
#   AFFICHER "Cette séance est complète"
#   RETOURNER au menu

#DEMANDER l'âge de chaque personne
#VERIFIER si l'âge correspond au type de billet
#SI l'âge n'est pas valide:
#   AFFICHER un message d'erreur
#   REDEMANDER l'âge

#SI type_billet == "vip":
#   DEMANDER si le client veut ajouter un repas
#   SI oui:
#       AJOUTER le prix du repas

#siege_choisis = choisir siege(liste_siege, nb_billet)
#VERIFIER si le siège existe
#SI le siège n'existe pas:
#   AFFICHER "Ce siège n'existe pas"

#SI le siège est déjà occupé:
#   AFFICHER "Siège occupé"
#   DEMANDER un autre siège

#SI le siège a déjà été choisi:
#   AFFICHER "Vous avez déjà choisi ce siège"

#SI le client entre 0:
#   ANNULER le choix des sièges
#   RETOURNER au menu

#AFFICHER le résumé de la réservation

#DEMANDER au client ce qu'il veut faire

#SI choix == 1:
#   CONFIRMER la réservation
#   ENREGISTRER les sièges occupés
#   CREER un numéro de réservation
#   CREER la facture

#SI choix == 2:
#   APPELER modifier_reservation()

#SI choix == 3:
#   ANNULER la réservation
#   AFFICHER "Réservation annulée"

#Calculer le prix de la réservation
#afficher "réservation effectué."
#creer_facture()
#############################################################################################
# afficher_horaire():
# AFFICHER horaire_film
#"0" pour retourner au menu principale
#############################################################################################
#Afficher_tarifs():
#AFFICHER tarifs
#"0" pour retourner au menu principale.
#############################################################################################
#creer_facture(type_billet, nb_billet, vip_nourriture, nom_client, nom_fil, siege_chosi)
#prix_billet = tarifs[type_billet]
#sous_total = prix unitaire * nb_billet
#SI vip_nourriture == vrai
#   #prix_sous_total = prix_sous_total + (prix_nourriture * nb_billet)
#prix_total = prix_sous_total * taux_taxes
#AFFICHER interface de facture -> nom du client, film, heure, nombre de billet, sieges, prix_total
#retourner prix total
#############################################################################################
#choisir_siege(liste_siege, nb_billet):
#liste_siege_choisi = []
#pour chaque siege dans Liste_siege
#   AFFICHER siege_disponibles
#
#for i in range nb_billet
#   Afficher "choisir une siege"
#       siege_choisi =
#   while siege_choisi == "occupeé"
#       AFFICHER "siège occupé. Veuillez en choisir un autre"
#       Ajouter liste_siege_choisi
#   retourner liste_siege_chosi
###############################################################################################
