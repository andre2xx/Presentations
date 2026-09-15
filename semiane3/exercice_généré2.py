# Exercice 2 : Validation et évaluation d'une note
def evaluer_note(note: float) -> str:
    if note >= 90:
        return "Excellent"
    elif note >= 80:
        return "Très bien"
    elif note >= 70:
        return "Bien"
    elif note >= 60:
        return "Passable"
    else:
        return "Échec"


# --- Exécution ---
saisie = input("Entrez votre note (0 à 100) : ")

# Validation de la donnée d'entrée
if saisie.replace('.', '', 1).isdigit():
    note_utilisateur = float(saisie)
    if 0 <= note_utilisateur <= 100:
        resultat = evaluer_note(note_utilisateur)
        print(f"Résultat pour {note_utilisateur}% : {resultat}")
    else:
        print("Erreur : La note doit être comprise entre 0 et 100.")
else:
    print("Erreur : Veuillez entrer un nombre valide.")