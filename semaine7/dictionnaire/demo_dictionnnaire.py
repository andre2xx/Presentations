
dictionnaire_vide = {}
dictionnaire_mots = {
    "lol" : "rire",
    "lego" : "blocs",
    "pc" : "ordi",
}



if "lol" in dictionnaire_mots:
    print("lol est dan sle dictionnaire")
else:
    print("le moty 'lol' n'est paas dans le dictionnaire")

if "lego" in dictionnaire_mots:
    print("lego est dans le dictionnaire")
else:
    print("Le mot 'lego' n'est pas dans le dictionnaire")

if "ordi" in dictionnaire_mots:
    print("ordi est dans le dictionnaire")
else:
    print("le mot 'ordi' n'estpas dans le dictionnaire")

dictionnaire_notes = {
    "Alice" : 80,
    "Bob" : 70,
    "Charlie" : 60,
    "David" : 100,
    "Fabrice" : 80,
    "Grégroire" : 40,
    "Hector" : 90
}
moyenne = (dictionnaire_notes["Alice"] + dictionnaire_notes["Bob"] + dictionnaire_notes["Charlie"] +dictionnaire_notes["David"]) / 4
print(moyenne)
moyenne = sum(dictionnaire_notes.values())/len(dictionnaire_notes)
print(moyenne)
nb_succes = 0
nb_echecs = 0
for nom, note in dictionnaire_notes.items():
    if note >= 60:
        nb_succes += 1
    else:
        nb_echecs += 1
print("Nombre d,étudiants qui ont passés:", nb_succes)
print("Nombre d'étudiants en échecs:", nb_echecs)
