import random
from datetime import datetime, timedelta

films = {
    "Avatar": 162,
    "Batman": 135,
    "Dune": 155,
    "Titanic": 195
}

# Générer l'horaire une seule fois
horaire = {}
salles = ["Salle 1", "Salle 2"]

for salle in salles:
    heure = datetime.strptime("10:00", "%H:%M")
    projections = []

    while heure < datetime.strptime("23:00", "%H:%M"):
        film = random.choice(list(films.keys()))
        duree = films[film]

        fin = heure + timedelta(minutes=duree)

        if fin > datetime.strptime("23:00", "%H:%M"):
            break

        projections.append({
            "film": film,
            "debut": heure.strftime("%H:%M"),
            "fin": fin.strftime("%H:%M")
        })

        # Pause de 15 minutes
        heure = fin + timedelta(minutes=15)

    horaire[salle] = projections

# Afficher l'horaire
for salle, projections in horaire.items():
    print(f"\n{salle}")

    for projection in projections:
        print(
            f'{projection["debut"]} - '
            f'{projection["fin"]} : '
            f'{projection["film"]}'
        )