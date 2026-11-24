################################################################################
# ENTRÉES :
# nom_client, choix_film, choix_horaire, nb_billets,
# type_billet, rangee, siege, avec_repas
#
# SORTIES :
# liste_films, horaires_films, liste_sieges,
# confirmation_reservation, facture, prix_total
#
# CONSTANTES :
# LISTE_FILMS, TARIFS, TAUX_TPS = 0.05,
# TAUX_TVQ = 0.09975, PRIX_REPAS_VIP = 7.00
#
# FONCTIONS :
# menu_principale(), creer_salle(), afficher_salle(),
# reserver_siege(), generer_dict_heure_film(),
# calculer_taxes_et_total(), option_liste_films(),
# option_horaire_films(), option_tarifs(),
# option_reserver_billet()
################################################################################

# menu_principale():

# CREER la salle de cinéma (4 rangées et 5 sièges)
# GENERER les horaires des films

# TANT QUE continuer == vrai:

#   AFFICHER le menu :
#       1- Liste des films
#       2- Réserver un billet
#       3- Horaire des films
#       4- Les tarifs
#       5- Quitter

#   DEMANDER le choix du client

#   SI choix == 1:
#       AFFICHER la liste des films

#   SI choix == 2:
#       APPELER option_reserver_billet()

#   SI choix == 3:
#       AFFICHER les horaires des films

#   SI choix == 4:
#       AFFICHER les tarifs

#   SI choix == 5:
#       AFFICHER "Merci et à bientôt !"
#       ARRETER le programme

#   SINON:
#       AFFICHER "Choix invalide"

################################################################################

# creer_salle():

# CREER une matrice de 4 rangées et 5 sièges
# INITIALISER tous les sièges à 0 (libres)
# RETOURNER la salle

################################################################################

# afficher_salle(salle):

# AFFICHER les rangées et les sièges

# SI siege == 0:
#     AFFICHER [O] (libre)
# SINON:
#     AFFICHER [X] (occupé)

################################################################################

# generer_dict_heure_film(films):

# DEFINIR les horaires possibles
# GENERER 3 horaires aléatoires pour chaque film
# EVITER les horaires en double
# RETOURNER les horaires des films

################################################################################

# reserver_siege(salle, rangee, siege):

# VERIFIER si la rangée et le siège existent

# SI le siège est occupé:
#     RETOURNER faux

# SINON:
#     MARQUER le siège comme occupé
#     RETOURNER vrai

################################################################################

# option_reserver_billet(salle, dict_heure_film):

# DEMANDER le nom du client
# VERIFIER que le nom n'est pas vide

# AFFICHER la liste des films
# DEMANDER le choix du film

# AFFICHER les horaires disponibles
# DEMANDER le choix de l'horaire

# DEMANDER le nombre de billets

# POUR chaque billet:

#     AFFICHER la salle

#     DEMANDER le numéro de rangée et de siège

#     VERIFIER si le siège existe et s'il est libre
#     VERIFIER si le siège a déjà été sélectionné

#     AFFICHER les types de billets
#     DEMANDER le type de billet

#     SI type_billet == VIP:
#         DEMANDER si le client veut un repas
#         SI oui:
#             AJOUTER 7.00 $ au prix du billet

#     AJOUTER le billet à la liste des billets réservés

# FIN POUR

# AFFICHER le résumé de la réservation
# AFFICHER le nom, le film, l'horaire et les sièges
# AFFICHER le sous-total

# AFFICHER les options :
#     1- Modifier le nom du client
#     2- Recommencer la sélection des billets
#     3- Confirmer et générer la facture

# DEMANDER le choix du client

# SI choix == 1:
#     MODIFIER le nom du client

# SI choix == 2:
#     RECOMMENCER la sélection des billets et sièges

# SI choix == 3:
#     RESERVER les sièges sélectionnés
#     CALCULER les taxes
#     GENERER la facture
#     CONFIRMER la réservation

################################################################################

# calculer_taxes_et_total(sous_total):

# CALCULER TPS = sous_total * 0.05
# CALCULER TVQ = sous_total * 0.09975
# CALCULER TOTAL = sous_total + TPS + TVQ

# RETOURNER TPS, TVQ et TOTAL

################################################################################

# option_liste_films():

# AFFICHER la liste des films disponibles

################################################################################

# option_horaire_films():

# AFFICHER les horaires de chaque film

################################################################################

# option_tarifs():

# AFFICHER les tarifs des billets
# AFFICHER le prix du repas VIP
# AFFICHER les taxes applicables

################################################################################

# FIN DU PROGRAMME
################################################################################