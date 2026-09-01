############################################
#Entrées: Température en celsius
#Sorties: Température em Fahrenheit
#Formule: F = celsius * 9/5 + 32
#temperature_celsius, temperature_fahrenheit
############################################








def convertir_fahrenheit():
    """
    permet de rentrer une températeure en Celsius et la convertir en fahrenheit
    :param:
    :return: fahrenheit
    """

    temperature_celsius = int(input("Entrer une température en degré celsius : "))

    temperature_fahrenheit = temperature_celsius * 9/5 +32

    print(f"Degré Fahrenheit : {temperature_fahrenheit}")




convertir_fahrenheit()

############################################
#Entrées: nombre de côtés, la longueur d’un côté, l’unité de mesure
#Sorties: Le périmètre du polygone est de 16cm
#Formule: longeur * nombre de coté
#nb_cote, longueur, unite_mesure, perimetre
############################################

def calculer_perimetre():
    """
    Permet de calculer le périmètre d'un polugone réguylier
    :return:
    """

    nb_cote = int(input("entrer le nombnre de coté du polygone régulier : "))

    longueur = float(input("Entrer les longeur des cotées : "))

    unite_mesure = input("entrer l'unité de mesure : ")

    perimetre = longueur * nb_cote

    print(f"Le périmètre du polygone est de {perimetre}{unite_mesure} ")


calculer_perimetre()



############################################
#Entrées: distance en Km, vitesse moyenne en Km/h
#Sorties: temps en heures et minutes
#Formule: T = distance / vitesse moyenne
# disance(km), vitesse_moyenne(km/h), temps_estimé(heure et minutes)
############################################

def calculer_temps():
    """
    Permet de calculer le temps estimé dL'un trajet selon la distyance et la vitesse moyenne en km/h.
    :return: durée du trtajet
    """


    distance = float(input("Entrer la distance de votre trajet : "))

    vitesse_moyenne = int(input("Entrer la vitesse moyenne en km/h: "))

    temps_estime = distance/vitesse_moyenne

    heures = int(temps_estime)
    minutes = int(temps_estime - heures) * 60

    print(f"{distance}km à une vitesse de {vitesse_moyenne}km/h = {heures}h{minutes}m")

calculer_temps()


############################################
#Entrées: mot de passe, min8imum de caractère
#Sorties: validité du mot de passe
#Formule:
# mot_passe, mion_car, valide
############################################


def valider_mot_passe(mot_passe:str, min_car: int)->bool:
    """
    Permet de valider un mot de passe
    :param mot_passe:
    :param min_car:
    :return: vrai ou faux si le mot de paasse et asser long
    """
    valide = len(mot_passe) >= min_car
    return valide


if __name__ == "__main__":
    mot_passe = input("Entrer un mot de passe : ")
    min_car = int(input("Entrer le nombre minimum de caractères: "))
    valide = valider_mot_passe(mot_passe,min_car)
    print(f"Mot de passe assez long: {valide}")


