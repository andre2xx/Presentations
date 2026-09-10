
def deposer(solde:float)->float:
    try:
        depot = float(input("Combien voulez vous déposer ?"))
        if depot < 0:
            print("Montant invalide")
        else:
            solde = solde + depot
    except:
        print("Ca doit etre un nombre")
    return solde

def retirer(solde:float)->float:
    try:
        retrait = float(input("combien voulez-vous retirez? "))
        if retrait > solde or retrait < 0:
            print("solde insuffisant")
        else:
            solde = solde - retrait

    except ValueError: # Gérer un type d'erreurs
        print("Ca doit etre un nombre")
    return solde




if __name__ == "__main__":
    solde = 100
    while True: # répeter
        choix = input("dépot ou retrait ou Quitter(D/R/Q: ")
        if choix == "R" or choix == "r": #Inclure les autres orthographe possible
            solde = retirer(solde)
        elif choix == "D" or choix == "d" or choix == "dépot":
            solde = deposer(solde)
        elif choix == "Q" or choix == "q":
            break
        else:
            print("choix invalide")
        print(f"solde : {solde}")

