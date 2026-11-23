# ============================================================
# GESTIONNAIRE DE RESERVATION DE SIEGES DE CINEMA
# ============================================================
import random
from datetime import date

# ------------------------------------------------------------
# DONNEES
# ------------------------------------------------------------
liste_films = [
    "Avengers Doomsday",
    "Scream 6",
    "Spiderman Brand New Day",
    "Toy Story 5"
]

# Quelle salle projette quel film
salle_du_film = {
    "Avengers Doomsday": 1,
    "Scream 6": 2,
    "Spiderman Brand New Day": 3,
    "Toy Story 5": 4
}

salles = {
    1: {
        "type": "Standard",
        "siege": [["A1", "A2", "A3", "A4", "A5"],
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"]]
    },
    2: {
        "type": "Standard",
        "siege": [["A1", "A2", "A3", "A4", "A5"],
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"]]
    },
    3: {
        "type": "Standard",
        "siege": [["A1", "A2", "A3", "A4", "A5"],
                  ["B1", "B2", "B3", "B4", "B5"],
                  ["C1", "C2", "C3", "C4", "C5"],
                  ["D1", "D2", "D3", "D4", "D5"]]
    },
    4: {
        "type": "Petite salle",
        "siege": [["A1", "A2", "A3", "A4"],
                  ["B1", "B2", "B3", "B4"],
                  ["C1", "C2", "C3", "C4"]]
    }
}

tarifs = {
    "enfants": 9.00,
    "adulte": 15.00,
    "etudiant": 12.00,
    "vip": 18.00
}

descriptions_billets = {
    "enfants": "Enfants (3-12 ans)",
    "adulte": "Adulte (13 ans et plus)",
    "etudiant": "Etudiant",
    "vip": "V.I.P. (18 ans et plus)"
}

# Âge minimum et maximum pour chaque type de billet
ages_billets = {
    "enfants": [3, 12],
    "adulte": [13, 120],
    "etudiant": [3, 120],
    "vip": [18, 120]
}

prix_repas = 7.00          # repas de la salle V.I.P., par billet
taux_taxes = 0.14975


# ------------------------------------------------------------
# HORAIRE ALEATOIRE QUI CHANGE CHAQUE JOUR
# ------------------------------------------------------------
def generer_horaire_du_jour():
    """Crée un dictionnaire {film: [heures]}.
     l'horaire est le même toute la journée,
    mais il change le lendemain."""
    random.seed(str(date.today()))
    horaire = {}
    for film in liste_films:
        heure = random.randint(10, 11)        # première séance à 10h ou 11h
        nb_seances = random.randint(4, 5)
        heures = []
        for i in range(nb_seances):
            minute = random.choice(["00", "30"])
            heures.append(str(heure) + ":" + minute)
            heure = heure + 3                 # une séance toutes les 3 heures
        horaire[film] = heures
    return horaire


horaire_films = generer_horaire_du_jour()

# Les sièges occupés de chaque séance (film + heure)

sieges_occupes = {}
for film in horaire_films:
    for heure in horaire_films[film]:
        sieges_occupes[film + " " + heure] = []

# La liste de toutes les réservations confirmées
reservations = []


# ------------------------------------------------------------
# FONCTIONS POUR DEMANDER DES INFORMATIONS (avec validation)
# Partout, taper 0 permet de retourner au menu principal.
# ------------------------------------------------------------
def demander_nombre(message, minimum, maximum):
    """Demande un nombre entier. Retourne None si l'utilisateur tape 0."""
    while True:
        try:
            nombre = int(input(message))
            if nombre == 0:
                return None
            elif nombre >= minimum and nombre <= maximum:
                return nombre
            else:
                print("Le nombre doit être entre", minimum, "et", maximum)
        except ValueError:
            print("Veuillez entrer un nombre entier.")


def choisir_dans_liste(titre, liste, texte_zero="Retourner au menu principal"):
    """Affiche une liste numérotée.
    """
    print(titre)
    for i in range(len(liste)):
        print(i + 1, "-", liste[i])
    print("0 -", texte_zero)

    choix = demander_nombre("Votre choix : ", 1, len(liste))
    if choix == None:
        return -1
    return choix - 1


def demander_nom():
    """Demande le nom du client. Retourne None si l'utilisateur tape 0."""
    while True:
        nom = input("Nom du client : ").strip()
        if nom == "0":
            return None
        elif nom == "":
            print("Le nom ne peut pas être vide.")
        else:
            nom_valide = True
            for lettre in nom:
                if lettre.isdigit():
                    nom_valide = False
            if nom_valide == True:
                return nom
            else:
                print("Le nom ne doit pas contenir de chiffres.")


def attendre_zero():
    """Attend que l'utilisateur tape 0 pour revenir au menu."""
    reponse = ""
    while reponse != "0":
        reponse = input("\nTapez 0 pour retourner au menu principal : ").strip()


# ------------------------------------------------------------
# FONCTIONS D'AFFICHAGE
# ------------------------------------------------------------
def afficher_film():
    print("\n===== LISTE DES FILMS =====")
    for film in liste_films:
        print("-", film, "(salle", salle_du_film[film], ")")
    attendre_zero()


def afficher_horaire():
    print("\n===== HORAIRES DES FILMS (" + str(date.today()) + ") =====")
    for film in horaire_films:
        print(film, ":", ", ".join(horaire_films[film]))
    attendre_zero()


def afficher_tarifs():
    print("\n===== TARIFS =====")
    for type_billet in tarifs:
        print(descriptions_billets[type_billet], ":", tarifs[type_billet], "$")
    print("Salle V.I.P. avec repas : +", prix_repas, "$ par billet (ajouté à la facture)")
    print("Taxes :", round(taux_taxes * 100, 3), "%")
    attendre_zero()


def afficher_sieges(film, heure):
    """Affiche la salle (liste 2D). [XX] veut dire que le siège est occupé."""
    numero_salle = salle_du_film[film]
    cle = film + " " + heure

    print("\n          ECRAN")
    print("-------------------------")
    for rangee in salles[numero_salle]["siege"]:
        ligne = ""
        for siege in rangee:
            if siege in sieges_occupes[cle]:
                ligne = ligne + "[XX] "
            else:
                ligne = ligne + "[" + siege + "] "
        print(ligne)


# ------------------------------------------------------------
# FONCTIONS POUR LES SIEGES
# ------------------------------------------------------------
def siege_existe(film, siege):
    """Retourne True si le siège existe dans la salle du film."""
    numero_salle = salle_du_film[film]
    for rangee in salles[numero_salle]["siege"]:
        if siege in rangee:
            return True
    return False


def compter_sieges_libres(film, heure):
    numero_salle = salle_du_film[film]
    total = 0
    for rangee in salles[numero_salle]["siege"]:
        total = total + len(rangee)
    occupes = len(sieges_occupes[film + " " + heure])
    return total - occupes


def choisir_siege(film, heure, nb_billet):
    """Demande les sièges un par un.
    Retourne la liste des sièges choisis, ou None si l'utilisateur tape 0."""
    cle = film + " " + heure
    liste_siege_choisi = []

    while len(liste_siege_choisi) < nb_billet:
        afficher_sieges(film, heure)
        if len(liste_siege_choisi) > 0:
            print("Déjà choisis :", liste_siege_choisi)

        numero = len(liste_siege_choisi) + 1
        siege = input("Choisir le siège " + str(numero) + " (0 pour annuler) : ").strip().upper()

        if siege == "0":
            return None
        elif siege_existe(film, siege) == False:
            print("Ce siège n'existe pas.")
        elif siege in sieges_occupes[cle]:
            print("Siège occupé. Veuillez en choisir un autre.")
        elif siege in liste_siege_choisi:
            print("Vous avez déjà choisi ce siège.")
        else:
            liste_siege_choisi.append(siege)

    return liste_siege_choisi


# ------------------------------------------------------------
# PRIX, RESUME ET FACTURE
# ------------------------------------------------------------
def calculer_prix(type_billet, nb_billet, vip_nourriture):
    """Retourne le sous-total, les taxes et le prix total."""
    sous_total = tarifs[type_billet] * nb_billet
    if vip_nourriture == True:
        sous_total = sous_total + prix_repas * nb_billet
    taxes = sous_total * taux_taxes
    prix_total = sous_total + taxes
    return sous_total, taxes, prix_total


def afficher_resume(reservation):
    sous_total, taxes, prix_total = calculer_prix(
        reservation["type_billet"], reservation["nb_billet"], reservation["vip_nourriture"])

    print("\n===== RESUME DE LA RESERVATION =====")
    print("Client      :", reservation["nom_client"])
    print("Film        :", reservation["film"])
    print("Heure       :", reservation["heure"])
    print("Salle       :", salle_du_film[reservation["film"]])
    print("Billets     :", reservation["nb_billet"], "x", descriptions_billets[reservation["type_billet"]])
    print("Sièges      :", reservation["sieges"])
    if reservation["type_billet"] == "vip":
        if reservation["vip_nourriture"] == True:
            print("Repas V.I.P.: oui")
        else:
            print("Repas V.I.P.: non")
    print(f"Total (taxes incluses) : {prix_total:.2f} $")


def creer_confirmation(reservation):
    print("\nRéservation effectuée.")
    print("Numéro de réservation :", reservation["numero"])
    print("Film :", reservation["film"], "à", reservation["heure"],
          "(salle", salle_du_film[reservation["film"]], ")")


def creer_facture(type_billet, nb_billet, vip_nourriture, nom_client, nom_film, heure_film, sieges):
    sous_total, taxes, prix_total = calculer_prix(type_billet, nb_billet, vip_nourriture)

    print("\n==============================")
    print("            FACTURE")
    print("==============================")
    print("Client      :", nom_client)
    print("Film        :", nom_film)
    print("Heure       :", heure_film)
    print("Salle       :", salle_du_film[nom_film])
    print("Sièges      :", sieges)
    print("------------------------------")
    print(f"{nb_billet} x {descriptions_billets[type_billet]} à {tarifs[type_billet]:.2f} $")
    if vip_nourriture == True:
        print(f"{nb_billet} x repas V.I.P. à {prix_repas:.2f} $")
    print("------------------------------")
    print(f"Sous-total  : {sous_total:.2f} $")
    print(f"Taxes       : {taxes:.2f} $")
    print(f"TOTAL       : {prix_total:.2f} $")
    print("==============================")

    return prix_total


# ------------------------------------------------------------
# MODIFIER UNE RESERVATION (avant de la confirmer)
# ------------------------------------------------------------
def modifier_reservation(reservation):
    """Modifie le dictionnaire 'reservation' directement."""
    choix = choisir_dans_liste(
        "\nQue voulez-vous modifier ?",
        ["Le nom du client", "Les sièges", "Le film et l'heure"],
        "Retour au résumé")

    if choix == 0:
        nouveau_nom = demander_nom()
        if nouveau_nom != None:
            reservation["nom_client"] = nouveau_nom

    elif choix == 1:
        nouveaux_sieges = choisir_siege(reservation["film"], reservation["heure"], reservation["nb_billet"])
        if nouveaux_sieges != None:
            reservation["sieges"] = nouveaux_sieges

    elif choix == 2:
        indice_film = choisir_dans_liste("\nFilms :", liste_films, "Retour au résumé")
        if indice_film != -1:
            nouveau_film = liste_films[indice_film]
            indice_heure = choisir_dans_liste("\nHeures :", horaire_films[nouveau_film], "Retour au résumé")
            if indice_heure != -1:
                nouvelle_heure = horaire_films[nouveau_film][indice_heure]
                if compter_sieges_libres(nouveau_film, nouvelle_heure) < reservation["nb_billet"]:
                    print("Il n'y a pas assez de places pour cette séance.")
                else:
                    print("Il faut choisir de nouveaux sièges pour cette séance.")
                    nouveaux_sieges = choisir_siege(nouveau_film, nouvelle_heure, reservation["nb_billet"])
                    if nouveaux_sieges != None:
                        reservation["film"] = nouveau_film
                        reservation["heure"] = nouvelle_heure
                        reservation["sieges"] = nouveaux_sieges


# ------------------------------------------------------------
# RESERVER DES BILLETS
# ------------------------------------------------------------
def reserver_billets():
    print("\n===== RESERVER DES BILLETS =====")
    print("(Tapez 0 à tout moment pour retourner au menu principal)")

    nom_client = demander_nom()
    if nom_client == None:
        return

    indice_film = choisir_dans_liste("\nFilms :", liste_films)
    if indice_film == -1:
        return
    nom_film = liste_films[indice_film]

    indice_heure = choisir_dans_liste("\nHeures :", horaire_films[nom_film])
    if indice_heure == -1:
        return
    heure_film = horaire_films[nom_film][indice_heure]

    # Est-ce qu'il reste des places ?
    sieges_libres = compter_sieges_libres(nom_film, heure_film)
    if sieges_libres == 0:
        print("Désolé, cette séance est complète.")
        return

    # Type de billet
    liste_types = list(tarifs.keys())
    textes_types = []
    for type_billet in liste_types:
        textes_types.append(descriptions_billets[type_billet] + " : " + str(tarifs[type_billet]) + " $")
    indice_type = choisir_dans_liste("\nTypes de billet :", textes_types)
    if indice_type == -1:
        return
    type_billet = liste_types[indice_type]

    # Nombre de billets : maximum 10, ou moins s'il reste moins de places
    maximum = sieges_libres
    if maximum > 10:
        maximum = 10
    nb_billet = demander_nombre("Nombre de billets (1 à " + str(maximum) + ") : ", 1, maximum)
    if nb_billet == None:
        return

    # Vérifier l'âge de chaque personne
    age_min = ages_billets[type_billet][0]
    age_max = ages_billets[type_billet][1]
    for i in range(nb_billet):
        age_valide = False
        while age_valide == False:
            age = demander_nombre("Âge de la personne pour le billet " + str(i + 1) + " : ", 1, 120)
            if age == None:
                return
            if age >= age_min and age <= age_max:
                age_valide = True
            else:
                print("Ce type de billet n'est pas valide pour cet âge (de", age_min, "à", age_max, "ans).")

    # Repas pour la salle V.I.P.
    vip_nourriture = False
    if type_billet == "vip":
        reponse = ""
        while reponse != "o" and reponse != "n" and reponse != "0":
            reponse = input("Ajouter le repas V.I.P. (+" + str(prix_repas) + " $ par billet) ? (o/n) : ").strip().lower()
        if reponse == "0":
            return
        if reponse == "o":
            vip_nourriture = True

    sieges = choisir_siege(nom_film, heure_film, nb_billet)
    if sieges == None:
        return

    # La réservation est un dictionnaire (pas encore confirmée)
    reservation = {
        "nom_client": nom_client,
        "film": nom_film,
        "heure": heure_film,
        "type_billet": type_billet,
        "nb_billet": nb_billet,
        "sieges": sieges,
        "vip_nourriture": vip_nourriture
    }

    # Résumé, puis confirmer / modifier / annuler
    termine = False
    while termine == False:
        afficher_resume(reservation)
        choix = choisir_dans_liste(
            "\nQue voulez-vous faire ?",
            ["Confirmer et créer la facture", "Modifier la réservation", "Annuler la réservation"],
            "Retourner au menu principal (annule la réservation)")

        if choix == 0:
            # On marque les sièges comme occupés
            cle = reservation["film"] + " " + reservation["heure"]
            for siege in reservation["sieges"]:
                sieges_occupes[cle].append(siege)

            numero = len(reservations) + 1
            reservation["numero"] = numero
            creer_confirmation(reservation)
            reservation["prix_total"] = creer_facture(
                reservation["type_billet"], reservation["nb_billet"], reservation["vip_nourriture"],
                reservation["nom_client"], reservation["film"], reservation["heure"],
                reservation["sieges"])
            reservations.append(reservation)
            attendre_zero()
            termine = True

        elif choix == 1:
            modifier_reservation(reservation)

        else:
            # choix == 2 (annuler) ou -1 (retour au menu)
            print("Réservation annulée.")
            termine = True


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------
def menu_principale():
    choix = ""
    while choix != "5":
        print("\n===== CINEMA - MENU PRINCIPAL =====")
        print("1- Liste des films")
        print("2- Réserver un billet")
        print("3- Horaires des films")
        print("4- Les tarifs")
        print("5- Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher_film()
        elif choix == "2":
            reserver_billets()
        elif choix == "3":
            afficher_horaire()
        elif choix == "4":
            afficher_tarifs()
        elif choix == "5":
            print("Merci et à bientôt !")
        else:
            print("Choix invalide. Entrez un nombre entre 1 et 5.")


# Lance le programme (cette ligne permet aussi d'importer le fichier dans les tests)
if __name__ == "__main__":
    menu_principale()