# Exercice 3 : Accumulateur de notes/nombres
somme = 0.0
compteur = 0

print("--- Saisie de nombres (entrez -1 pour terminer) ---")

while True:
    saisie = input("Entrez un nombre positif (-1 pour quitter) : ")

    if saisie == "-1":
        break  # Condition d'arrêt

    if saisie.replace('.', '', 1).isdigit():
        valeur = float(saisie)
        if valeur < 0:
            print("Veuillez entrer un nombre positif.")
        else:
            somme += valeur
            compteur += 1
    else:
        print("Entrée invalide.")

if compteur > 0:
    moyenne = somme / compteur
    print(f"\nNombre de valeurs : {compteur}")
    print(f"Somme totale : {somme:.2f}")
    print(f"Moyenne : {moyenne:.2f}")
else:
    print("Aucune donnée valide n'a été saisie.")