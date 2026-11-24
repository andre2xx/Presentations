
import random


TAUX_TPS = 0.05
TAUX_TVQ = 0.09975
PRIX_REPAS_VIP = 7.0  # Option repas VIP


LISTE_FILMS = [
    "Avanger doomsday",
    "Scream 6",
    "Spiderman brand new day",
    "Toy Story 5"
]

#TARIFS DES BILLETS
TARIFS = {
    "1": {"nom": "Enfant (3-12ans)", "prix": 9.0},
    "2": {"nom": "Étudiant", "prix": 12.0},
    "3": {"nom": "Adulte (13 ans et plus)", "prix": 15.0},
    "4": {"nom": "V.I.P (18 ans et plus)", "prix": 18.0}
}


def creer_salle(nb_rangees=4, nb_sieges=5):
    """Crée une matrice 2D de 0 pour la salle de cinéma.

    """
    salle = []
    for r in range(nb_rangees):
        rangee = []
        for s in range(nb_sieges):
            rangee.append(0)
        salle.append(rangee)
    return salle


def afficher_salle(salle):
    """Affiche la grille 2D de la salle de cinéma.

    """
    print("\n--- ECRAN DU CINEMA ---")
    num_rangee = 1
    for rangee in salle:
        ligne = "Rangée " + str(num_rangee) + " : "
        for siege in rangee:
            if siege == 1:
                ligne = ligne + "[X] "
            else:
                ligne = ligne + "[O] "
        print(ligne)
        num_rangee = num_rangee + 1
    print("-----------------------\n[O] = Libre  |  [X] = Occupé\n")


def reserver_siege(salle, rangee, siege):
    """Réserve un siège s'il est disponible (0).

    """
    if rangee < 0 or rangee >= len(salle):
        return False
    if siege < 0 or siege >= len(salle[0]):
        return False

    if salle[rangee][siege] == 1:
        return False
    else:
        salle[rangee][siege] = 1
        return True


def generer_dict_heure_film(films):
    """Génère un dictionnaire d'horaires aléatoires pour chaque film.

    """
    dict_heure_film = {}
    heures_possibles = ["13:00", "15:30", "18:00", "20:30", "22:00"]

    for film in films:
        h1 = random.choice(heures_possibles)
        h2 = random.choice(heures_possibles)
        h3 = random.choice(heures_possibles)

        horaires = []
        if h1 not in horaires:
            horaires.append(h1)
        if h2 not in horaires:
            horaires.append(h2)
        if h3 not in horaires:
            horaires.append(h3)

        dict_heure_film[film] = horaires

    return dict_heure_film


def calculer_taxes_et_total(sous_total):
    """Calcule la TPS, la TVQ et le total.

    """
    tps = sous_total * TAUX_TPS
    tvq = sous_total * TAUX_TVQ
    total = sous_total + tps + tvq
    return tps, tvq, total


#OPTION 1 : LISTE FILMS
def option_liste_films():
    """Affiche la liste des films projetés.

    """
    print("\n==========================================")
    print("         LISTE DES FILMS À L'AFFICHE      ")
    print("==========================================")
    for i in range(len(LISTE_FILMS)):
        print(str(i + 1) + ". " + LISTE_FILMS[i])
    print("==========================================\n")
    input("Appuyez sur Entrée pour retourner au menu principal...")


#OPTION 3 : HORAIRE DES FILMS
def option_horaire_films(dict_heure_film):
    """Affiche l'horaire des films.

    """
    print("\n==========================================")
    print("            HORAIRES DES FILMS            ")
    print("==========================================")
    for film in dict_heure_film:
        horaires = dict_heure_film[film]
        horaires_texte = ""
        for h in horaires:
            horaires_texte = horaires_texte + h + "  "
        print("- " + film + " : " + horaires_texte)
    print("==========================================\n")
    input("Appuyez sur Entrée pour retourner au menu principal...")


#OPTION 4 : LES TARIFS
def option_tarifs():
    """Affiche les tarifs des billets.

    """
    print("\n==========================================")
    print("           TARIFS DES BILLETS             ")
    print("==========================================")
    print("1- Enfant (3-12ans)        : 9.00 $")
    print("2- Étudiant                : 12.00 $")
    print("3- Adulte (13 ans et plus)  : 15.00 $")
    print("4- V.I.P (18 ans et plus)   : 18.00 $")
    print("------------------------------------------")
    print("Option Salle V.I.P avec repas: +7.00 $")
    print("Taxes applicables : TPS (5.0%) et TVQ (9.975%)")
    print("==========================================\n")
    input("Appuyez sur Entrée pour retourner au menu principal...")


# --- OPTION 2 : RESERVER BILLET ---
def option_reserver_billet(salle, dict_heure_film):
    """Création d'une réservation avec menu de modification et facture.

    """
    print("\n==========================================")
    print("        RÉSERVATION DE BILLETS           ")
    print("==========================================")


    nom_client = input("Entrez le nom du client : ").strip()
    while nom_client == "":
        print("Le nom ne peut pas être vide.")
        nom_client = input("Entrez le nom du client : ").strip()

    #Choix du film
    print("\nChoix du film :")
    for i in range(len(LISTE_FILMS)):
        print(str(i + 1) + ". " + LISTE_FILMS[i])

    while True:
        try:
            choix_f = int(input("Votre choix (1-4) : "))
            if 1 <= choix_f <= len(LISTE_FILMS):
                film_choisi = LISTE_FILMS[choix_f - 1]
                break
            else:
                print("Veuillez choisir un film entre 1 et 4.")
        except ValueError:
            print("Entrez un nombre entier.")

    #Choix de l'horaire
    horaires = dict_heure_film[film_choisi]
    print("\nHoraires disponibles pour " + film_choisi + " :")
    for i in range(len(horaires)):
        print(str(i + 1) + ". " + horaires[i])

    while True:
        try:
            choix_h = int(input("Votre choix d'horaire : "))
            if 1 <= choix_h <= len(horaires):
                horaire_choisi = horaires[choix_h - 1]
                break
            else:
                print("Choix d'horaire invalide.")
        except ValueError:
            print("Entrez un nombre entier.")

    en_creation = True
    while en_creation:
        # Nombre de billets
        while True:
            try:
                nb_billets = int(input("\nCombien de billets souhaitez-vous réserver ? : "))
                if nb_billets > 0:
                    break
                else:
                    print("Entrez un nombre supérieur à 0.")
            except ValueError:
                print("Entrez un nombre entier.")

        billets_reserves = []

        for idx in range(nb_billets):
            print("\n--- Billet " + str(idx + 1) + " sur " + str(nb_billets) + " ---")
            afficher_salle(salle)

            # Choix du siège (grille 2D)
            while True:
                try:
                    r = int(input("Numéro de rangée (1 à 4) : ")) - 1
                    s = int(input("Numéro de siège (1 à 5) : ")) - 1

                    if 0 <= r < len(salle) and 0 <= s < len(salle[0]):
                        # Vérifier si déjà choisi dans cette session
                        deja_choisi = False
                        for b in billets_reserves:
                            if b["rangee"] == r and b["siege"] == s:
                                deja_choisi = True
                                break

                        if salle[r][s] == 0 and not deja_choisi:
                            break
                        else:
                            print("Ce siège est déjà réservé [X] ou déjà sélectionné.")
                    else:
                        print("Rangée (1-4) ou siège (1-5) invalide.")
                except ValueError:
                    print("Entrez un nombre entier.")

            #Choix du type de billet
            print("\nType de billet :")
            print("1. Enfant (3-12ans) - 9.00 $")
            print("2. Étudiant - 12.00 $")
            print("3. Adulte (13 ans et plus) - 15.00 $")
            print("4. V.I.P (18 ans et plus) - 18.00 $")

            while True:
                choix_t = input("Votre choix (1-4) : ").strip()
                if choix_t in TARIFS:
                    info = TARIFS[choix_t]
                    type_nom = info["nom"]
                    prix = info["prix"]
                    avec_repas = False

                    if choix_t == "4":
                        print("\nOption Salle V.I.P : Voulez-vous le repas (+7.00 $) ?")
                        print("1. Oui")
                        print("2. Non")
                        rep = input("Votre choix (1-2) : ").strip()
                        if rep == "1":
                            avec_repas = True
                            prix = prix + PRIX_REPAS_VIP
                    break
                else:
                    print("Choix invalide. Choisissez entre 1 et 4.")

            billets_reserves.append({
                "rangee": r,
                "siege": s,
                "type": type_nom,
                "prix": prix,
                "avec_repas": avec_repas
            })

        #Résumé et option de modification
        while True:
            print("\n==========================================")
            print("         RÉSUMÉ DE LA RÉSERVATION         ")
            print("==========================================")
            print("Nom du client : " + nom_client)
            print("Film          : " + film_choisi)
            print("Horaire       : " + horaire_choisi)
            print("Billets sélectionnés :")

            sous_total = 0.0
            for idx_b in range(len(billets_reserves)):
                b = billets_reserves[idx_b]
                sous_total = sous_total + b["prix"]
                txt_repas = " (avec repas)" if b["avec_repas"] else ""
                print("  " + str(idx_b + 1) + ". Rangée " + str(b["rangee"] + 1) + ", Siège " + str(
                    b["siege"] + 1) + " - " + b["type"] + txt_repas + " : " + f"{b['prix']:.2f}" + " $")

            print("Sous-total : " + f"{sous_total:.2f}" + " $")
            print("==========================================")

            print("\nOption de réservation :")
            print("1- Modifier le nom du client")
            print("2- Recommencer la sélection des billets et sièges")
            print("3- Confirmer et générer la facture")

            choix_mod = input("Votre choix (1-3) : ").strip()

            if choix_mod == "1":
                nom_client = input("Nouveau nom du client : ").strip()
                while nom_client == "":
                    print("[ERREUR] Le nom ne peut pas être vide.")
                    nom_client = input("Nouveau nom du client : ").strip()
                print("[OK] Nom mis à jour.")

            elif choix_mod == "2":
                print("[INFO] Recommencement de la sélection...")
                break

            elif choix_mod == "3":
                # Valider les sièges dans la matrice 2D
                for b in billets_reserves:
                    reserver_siege(salle, b["rangee"], b["siege"])

                # Facture finale avec taxes
                tps, tvq, total = calculer_taxes_et_total(sous_total)

                print("\n==========================================")
                print("             FACTURE OFFICIELLE           ")
                print("==========================================")
                print("Client  : " + nom_client)
                print("Film    : " + film_choisi)
                print("Horaire : " + horaire_choisi)
                print("------------------------------------------")
                for b in billets_reserves:
                    txt_r = " + Repas (7$)" if b["avec_repas"] else ""
                    print("Rangée " + str(b["rangee"] + 1) + ", Siège " + str(b["siege"] + 1) + " | " + b[
                        "type"] + txt_r + " : " + f"{b['prix']:.2f}" + " $")
                print("------------------------------------------")
                print("Sous-total     : " + f"{sous_total:.2f}" + " $")
                print("TPS (5.0%)     : " + f"{tps:.2f}" + " $")
                print("TVQ (9.975%)   : " + f"{tvq:.2f}" + " $")
                print("TOTAL À PAYER  : " + f"{total:.2f}" + " $")
                print("==========================================")
                print("[OK] Réservation confirmée et facture créée !\n")

                en_creation = False
                break
            else:
                print("Option invalide (1, 2 ou 3).")

    input("Appuyez sur Entrée pour retourner au menu principal...")


#MENU PRINCIPAL
def menu_principale():
    salle = creer_salle(4, 5)
    dict_heure_film = generer_dict_heure_film(LISTE_FILMS)
    continuer = True

    while continuer:
        print("\n==========================================")
        print(" GESTIONNAIRE DE RÉSERVATION DE CINÉMA  ")
        print("==========================================")
        print("1- Liste des films")
        print("2- Réserver un billet")
        print("3- Horaire des films")
        print("4- Les tarifs")
        print("5- Quitter")

        choix = input("Votre choix (1-5) : ").strip()

        if choix == "1":
            option_liste_films()
        elif choix == "2":
            option_reserver_billet(salle, dict_heure_film)
        elif choix == "3":
            option_horaire_films(dict_heure_film)
        elif choix == "4":
            option_tarifs()
        elif choix == "5":
            print("\nMerci d'avoir choisi notre cinéma. À bientôt !")
            continuer = False
        else:
            print("Option invalide. Entrez un chiffre de 1 à 5.")





if __name__ == "__main__":
    menu_principale()