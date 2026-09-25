liste_transaction = []
def deposer(solde):
    montant = float(input("combien vouolez vous déposer ? : "))
    solde = solde + montant
    return solde
def retirer(solde):
    montant = float(input("Montant à retirer : "))
    if montant > solde:
        print("fonds insuffisants")
    else:
        sole = solde - montant
        liste_transaction.append(-montant)
        return solde

    while True:
        choix = input("Dépot ou retrait (D/R/Q)? : ")
        if choix == "R" or choix == "r":
            solde = retirer(solde)
        elif choix == "D" or choix == "d" or choix == "Dépôt":
            solde = deposer(solde)
        elif choix == "Q" or choix == "Q":
            break
        else:
            print("choix invbalide")
        print(f"Solde : {solde:.2f}")

    print("-" * 10, "transaction", "-" * 10)
    for i in range(len(liste_transaction)):
        print(f"Transaction {i} : {liste_transaction[i]:>20.2f}")
    print("-" * 34)
    print(f"Solde :     {solde:>20.2f}")


    #TODO : afficher le nombre de dépots et de retraits
    #TODO :`aafficher les montants des retraits

