# Exercice 4 : Trouvez l'erreur logique grâce au débogueur !
def calculer_total_facture(liste_prix: list, taxe_pourcent: float) -> float:
    total = 0.0
    # PISTE : Observez ce qui arrive à 'total' à chaque tour de boucle !
    for prix in liste_prix:
        total += prix + (prix * (taxe_pourcent / 100))
    return total


prix_articles = [10.0, 25.0, 15.0]
taux_taxe = 15.0

total_obtenu = calculer_total_facture(prix_articles, taux_taxe)
print(f"Total calculé : {total_obtenu:.2f} $ (Attendu : 57.50 $)")