"""
initialisé le solde
afficher le solde
demaander combien on veut déposer
stocker l'argent : additioner avbec dépot
affciher le nouveau solde
************************
retrait:
demander on vient retirer
soustraire le retrait du solde
afficher le nouveau solde
"""

solde = 100
print("Solde : ", solde)
depot= float(input("combien vouolez vous déposer ? : "))
solde = solde + depot
print(f"Solde : {solde:.2f}")
retrait = float(input("combien voulez-vous retirez? "))
solde = solde    - retrait
print("-"*10, "Transaction", "-" * 10)
print(f"Dépot : {depot:>20.2f}")# >alligner a droite
print(f"Retrait: {retrait:>20.2f}")# et colonne de largeur 20
print("-"* 34)
print(f"Solde : {solde:.2f}")

