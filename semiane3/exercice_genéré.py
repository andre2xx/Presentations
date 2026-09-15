# Exercice 1 : Calcul de rabais
def calculer_prix_rabais(prix_initial: float, pourcentage_rabais: float) -> float:
    """
    Calcule le prix final après application d'un rabais.

    :param prix_initial: Le prix de base (float)
    :param pourcentage_rabais: Le pourcentage de rabais entre 0 et 100 (float)
    :return: Le prix final après rabais (float)
    """
    montant_rabais = prix_initial * (pourcentage_rabais / 100)
    prix_final = prix_initial - montant_rabais
    return prix_final


# --- Exécution ---
prix = 80.0
rabais = 15.0
prix_reduit = calculer_prix_rabais(prix, rabais)

print(f"Prix initial : {prix:.2f} $")
print(f"Rabais appliqué : {rabais}%")
print(f"Prix final : {prix_reduit:.2f} $")g