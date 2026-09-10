TAUX_TAXES = 14.997 #Constante, en masjuscules - En haut : Globale

def calculer_facture(prix:float, quantite:int) ->float: #paramètre, variables locales, existant juste dans la fonction
    """
    calculer le total de la facture
    """


    sous_total = prix * quantite
    total = sous_total + sous_total*TAUX_TAXES/100
    return total


if __name__ == "__main__":
    prix_unitaire = 10 #prix_unitaire. quantite : variable locale : existe juste dansle programme principale
    quantite = 2
    prix_total = calculer_facture(prix_unitaire, quantite)
    print("Prix unitaire:", prix_unitaire) # MARCHE PAS AVEC RPIX, PRIX EST SEULEMENT DANS LA FONCTION
    print("Qunatite: ",quantite)
    print("Taux de taxes: ",TAUX_TAXES)
    print(f"{prix_total:.2f}")