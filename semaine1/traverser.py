feu = input("Le feu est de quelle couleur? (rouge/vert/orange)") # vert, orange
barriere_ouvert = bool(input("est-ce que la barrière est ouverte ? (sinon appuyer sur entrer)"))#Bool : False
# traverser = (feu == "vert" or (feu == "rouge" and barriere_ouvert == True))
if feu == "vert":
    print("on peut traverser")
elif feu == "rouge" and barriere_ouvert:
    print("on peut traverser!")
else:
    print("on ne peut pas traverser")
