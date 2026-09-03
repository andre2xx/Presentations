solde = 100
choix = input("Dépot ou retrait (D/R)? : ")
if choix == "R" or choix == "r":
    retrait = float(input("combien voulez-vous retirez? "))
    if retrait > solde:
        print("solde insuffisant")
    else:
        solde = solde - retrait

elif choix == "D " or "d":
    depot = float(input("combien vouolez vous déposer ? : "))
    solde = solde + depot
print(f"Solde :  {solde:.2f}")

